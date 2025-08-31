# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WaveMakeAPP_Main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QSplitter, QStatusBar, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(897, 591)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_noise_btn = QPushButton(self.centralwidget)
        self.add_noise_btn.setObjectName(u"add_noise_btn")
        self.add_noise_btn.setGeometry(QRect(760, 440, 101, 32))
        self.noise_amp_slider = QSlider(self.centralwidget)
        self.noise_amp_slider.setObjectName(u"noise_amp_slider")
        self.noise_amp_slider.setGeometry(QRect(20, 440, 721, 25))
        self.noise_amp_slider.setOrientation(Qt.Orientation.Horizontal)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(20, 410, 141, 20))
        font = QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(20, 380, 201, 20))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.canvas = QWidget(self.centralwidget)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setGeometry(QRect(30, 70, 831, 231))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(20, 330, 111, 18))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(360, 330, 141, 18))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.noise_freq_input = QSpinBox(self.centralwidget)
        self.noise_freq_input.setObjectName(u"noise_freq_input")
        self.noise_freq_input.setGeometry(QRect(230, 380, 101, 22))
        self.wave_type = QComboBox(self.centralwidget)
        self.wave_type.setObjectName(u"wave_type")
        self.wave_type.setGeometry(QRect(130, 320, 96, 32))
        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")
        self.draw_button.setGeometry(QRect(730, 320, 131, 41))
        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(260, 490, 131, 41))
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(480, 490, 131, 41))
        self.freq_box = QSpinBox(self.centralwidget)
        self.freq_box.setObjectName(u"freq_box")
        self.freq_box.setGeometry(QRect(500, 330, 101, 22))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 30, 164, 27))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.splitter.addWidget(self.label_3)
        self.channel_selector = QComboBox(self.splitter)
        self.channel_selector.setObjectName(u"channel_selector")
        self.splitter.addWidget(self.channel_selector)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 897, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_noise_btn.setText(QCoreApplication.translate("MainWindow", u"Add Noise", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Noise Amplitube:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Noise Frequency (Hz):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Wave Type:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz):", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"Draw Waveform", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send to Arduino", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save as Header File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

