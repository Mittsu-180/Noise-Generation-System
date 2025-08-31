from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QFileDialog, QHBoxLayout, QGridLayout, QWidget, QSizePolicy,
    QMessageBox
)
from PySide6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import serial
import serial.tools.list_ports
from WaveMakeAPP_Main import Ui_MainWindow



class WaveformEditor(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(WaveformEditor, self).__init__(parent)
        self.setWindowTitle("Waveform Editor for Arduino")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 最初にUIファイルを読み込み

        # コンボボックスなどの初期化
        self.ui.wave_type.addItems(["Sine", "Square", "Noise"])
        self.ui.freq_box.setRange(1, 1000)
        self.ui.freq_box.setValue(50)
        self.ui.channel_selector.addItems(["CH1", "CH2", "CH3", "CH4"])
        self.ui.noise_freq_input.setRange(0, 100000)
        self.ui.noise_freq_input.setValue(1000)

        self.waves = {
            "CH1": None,
            "CH2": None,
            "CH3": None,
            "CH4": None,
        }

        # レイアウト再構築
        self._setup_layouts()

        # ボタン接続（レイアウト構築後に実行）
        self.ui.add_noise_btn.clicked.connect(self.add_noise_to_current_wave)
        self.ui.draw_button.clicked.connect(self.draw_waveform)
        self.ui.send_button.clicked.connect(self.send_to_arduino)
        self.ui.save_button.clicked.connect(self.save_header)
       

    def draw_waveform(self):
        fs = 6000
        t = np.linspace(0, 1, fs, endpoint=False)
        freq = self.ui.freq_box.value()


        if self.ui.wave_type.currentText() == "Sine":
            sig = 0.5 * np.sin(2 * np.pi * freq * t)
        elif self.ui.wave_type.currentText() == "Square":
            sig = 0.5 * np.sign(np.sin(2 * np.pi * freq * t))
        else:
            base = 0.5 * np.sin(2 * np.pi * freq * t)
            noise = 0.2 * np.random.randn(len(t))
            sig = base + noise
            # sig = 0.2 * np.random.randn(len(t))

        self.current_wave = sig
        self.data = ((sig - sig.min()) / (sig.max() - sig.min()) * 255).astype(np.uint8)
        print("Waveform generated. Data length:", len(self.data))


        self.ax.clear()
        self.ax.plot(self.data) # 最初の500点だけ表示
        self.ax.set_title("Waveform Preview")
        self.canvas.draw()

        channel = self.ui.channel_selector.currentText()
        self.waves[channel] = sig # 元の波形(float)
        self.data = ((sig - sig.min()) / (sig.max() - sig.min()) * 255).astype(np.uint8)


    def save_header(self):
        if self.data is None:
            return
        
        path, _ = QFileDialog.getSaveFileName(self, "Save Header", "", "Header Files (*.h)")
        if not path:
            return
        
        with open(path, "w") as f:
            f.write("#ifndef WAVE_TABLE_H\n#define WAVE_TABLE_H\n#include <avr/pgmspace.h>\n")
            for ch in ["CH1", "CH2", "CH3", "CH4"]:
                sig = self.waves.get(ch)
                if sig is None:
                    sig = np.zeros(256)
                data = ((sig - sig.min()) / (sig.max() - sig.min()) * 255).astype(np.uint8)
                f.write(f"const uint8_t {ch}[] PROGMEM = {{{','.join(map(str, data))}}};\n")
            f.write("const int WAVE_LENGTH = 6000;\n\n#endif")


    def send_to_arduino(self):
        all_data = []
        for ch in ["CH1", "CH2", "CH3", "CH4"]:
            sig = self.waves.get(ch)
            if sig is None:
                sig = np.zeros(256)
            # 正規化してuint8に変換
            normalized = ((sig - sig.min()) / (sig.max() - sig.min()) * 255).astype(np.uint8)
            all_data.extend(normalized)

        final_data = bytes([0xFF]) + bytes(all_data)

        # 使用可能なポート一覧から選ぶ（最初のポートに接続）
        ports = list(serial.tools.list_ports.comports())
        if not ports:
            print("No serial ports found.")
            return

        port_name = ports[0].device  # 例: COM3, /dev/ttyUSB0 など
        try:
            with serial.Serial(port_name, 115200, timeout=1) as ser:
                ser.write(final_data)  # 開始マーカー（255）
                print(f"Sent {len(final_data)} bytes to {port_name}")
        except Exception as e:
            print(f"Error sending to Arduino: {e}")
    


    def add_noise_to_current_wave(self):
        channel = self.ui.channel_selector.currentText()
        if self.waves[channel] is None:
            QMessageBox.warning(self, "エラー", f"{channel} に波形がありません。")
            return
        
        original = self.waves[channel].astype(float)
        if self.current_wave is None:
            QMessageBox.warning(self, "エラー", "波形が選択されていません。")
            return
        
        freq = float(self.ui.noise_freq_input.text())
        amp = self.ui.noise_amp_slider.value() / 100
        t = np.linspace(0, 1, len(self.current_wave), endpoint=False)
        noise = amp * np.sin(2 * np.pi * freq * t)

        original = self.current_wave.astype(float)
        mixed = original + noise
        mixed = ((mixed - mixed.min()) / (mixed.max() - mixed.min()) * 255).astype(np.uint8)

        self.current_wave = mixed
        self.update_plot(mixed)
        self.waves[channel] = mixed


    def update_plot(self, wave):
        self.ax.clear()
        self.ax.plot(wave)
        self.ax.set_title("Waveform Preview")
        self.canvas.draw()
        self.data = wave.astype(np.uint)


    def _setup_layouts(self):
    # 中央ウィジェットのレイアウトをクリア
        central_widget = self.ui.centralwidget
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # チャンネル選択部分
        channel_layout = QHBoxLayout()
        channel_layout.addWidget(self.ui.label_3)
        channel_layout.addWidget(self.ui.channel_selector)
        channel_layout.addStretch()
        
        # キャンバス部分（MatplotlibのFigureを配置）
        self.canvas = FigureCanvas(plt.Figure())
        canvas_layout = QVBoxLayout(self.ui.canvas)
        canvas_layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.subplots()
        
        # 波形設定部分
        wave_settings_layout = QHBoxLayout()
        wave_settings_layout.addWidget(self.ui.label_4)
        wave_settings_layout.addWidget(self.ui.wave_type)
        wave_settings_layout.addWidget(self.ui.label_5)
        wave_settings_layout.addWidget(self.ui.freq_box)
        wave_settings_layout.addStretch()
        wave_settings_layout.addWidget(self.ui.draw_button)
        
        # ノイズ設定部分
        noise_settings_layout = QGridLayout()
        noise_settings_layout.addWidget(self.ui.label_6, 0, 0)
        noise_settings_layout.addWidget(self.ui.noise_freq_input, 0, 1)
        noise_settings_layout.addWidget(self.ui.label_7, 1, 0)
        noise_settings_layout.addWidget(self.ui.noise_amp_slider, 1, 1)
        noise_settings_layout.addWidget(self.ui.add_noise_btn, 1, 2)
        
        # ボタン部分（送信/保存）
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ui.send_button)
        button_layout.addWidget(self.ui.save_button)
        button_layout.addStretch()
        
        # メインレイアウトに全要素を追加
        main_layout.addLayout(channel_layout)
        main_layout.addWidget(self.ui.canvas)
        main_layout.addLayout(wave_settings_layout)
        main_layout.addLayout(noise_settings_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        
        # サイズポリシー設定（リサイズ時に拡大）
        self.ui.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # 初期サイズ設定
        self.resize(897, 591)



if __name__ == "__main__":
    app = QApplication([])
    editor = WaveformEditor()
    editor.show()
    app.exec()