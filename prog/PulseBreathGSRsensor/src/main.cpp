#include <Arduino.h>

#define ANALOG_PIN_1 0
int analog_value = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Analog IN Test");
}

void loop() {
  // put your main code here, to run repeatedly:
  analog_value = analogRead(ANALOG_PIN_1);
  Serial.println(analog_value);
  delay(500);
  
}