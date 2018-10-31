/*#include <Arduino.h>

#define ANALOG_PIN_0 0
float analog_value0 = 0;

#define GSR_RESISTOR 1000000000
#define ANALOG_PIN_2 2
float analog_value2 = 0;

#define Breath_RESISTOR 1000000
#define ANALOG_PIN_14 14
float analog_value14 = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Analog IN Test");
}

void loop() {
  // put your main code here, to run repeatedly:
  analog_value0 = analogRead(ANALOG_PIN_0);
  Serial.println("Pulse sensor: " + String(analog_value0));
  analog_value2 = analogRead(ANALOG_PIN_2);
  Serial.println("GSR sensor: " + String(analog_value2));
  analog_value14 = analogRead(ANALOG_PIN_14);
  Serial.println("Breath sensor: " + String(analog_value14));
  delay(500);
  
  // (10)/20-50 milliseconden sample rate
}*/

//  float R = (SERIESRESISTOR * analog_value / (1023 - analog_value)) * (-1);