#include <Arduino.h>
#include "Test1.h" \\使用するヘッダファイル名を記入
#include <avr/pgmspace.h>


const int pin1 = 9;
const int pin2 = 10;
const int pin3 = 11;
const int pin4 = 12;


const int WAVE_SIZE = 256;
uint8_t ch1_buffer[WAVE_SIZE];
uint8_t ch2_buffer[WAVE_SIZE];
uint8_t ch3_buffer[WAVE_SIZE];
uint8_t ch4_buffer[WAVE_SIZE];
bool use_received_wave = false;


int i = 0;

void setup() {
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);


  Serial.begin(115200);
  while(!Serial);

  Serial.println("Ready to receive waveform or use built-in wave.");
  
}

void loop(){
  if (Serial.available()) {
    if(Serial.read() == 0xFF) {
      int received = 0;
      while (received < WAVE_SIZE) {
        if (Serial.available() >= 4) {
          ch1_buffer[received] = Serial.read();
          ch2_buffer[received] = Serial.read();
          ch3_buffer[received] = Serial.read();
          ch4_buffer[received] = Serial.read();
          received++;
        }
      }
      use_received_wave = true;
      Serial.println("Received waveform from PC.");
    }
  }

  if (use_received_wave) {
    analogWrite(pin1, ch1_buffer[i]);
    analogWrite(pin2, ch2_buffer[i]);
    analogWrite(pin3, ch3_buffer[i]);
    analogWrite(pin4, ch4_buffer[i]);
  }else {
    analogWrite(pin1, pgm_read_byte(&(CH1[i])));
    analogWrite(pin2, pgm_read_byte(&(CH2[i])));
    analogWrite(pin3, pgm_read_byte(&(CH3[i])));
    analogWrite(pin4, pgm_read_byte(&(CH4[i])));
  }


  i++;
  if (i >= WAVE_SIZE) i = 0;

  delayMicroseconds(125);
}