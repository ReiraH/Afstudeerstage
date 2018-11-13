#include <Arduino.h>
#include <time.h>

#define ANALOG_PIN_0 0
float analog_value0 = 0;

#define GSR_RESISTOR 1000000000
#define ANALOG_PIN_2 2
float analog_value2 = 0;

#define Breath_RESISTOR 1000000
#define ANALOG_PIN_14 14
float analog_value14 = 0;

unsigned long aTime;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Analog IN Test");
}

void loop() {
  // put your main code here, to run repeatedly:
  aTime = millis();
  analog_value0 = analogRead(ANALOG_PIN_0);
  analog_value14 = analogRead(ANALOG_PIN_14);
  analog_value2 = analogRead(ANALOG_PIN_2);
  
  Serial.println("t: " + String(aTime) + 
                " p: " + String(analog_value0) + 
                " b: " + String(analog_value14) + 
                " g: " + String(analog_value2));
  delay(20);
  
  // (10)/20-50 milliseconden sample rate
}

//  float R = (SERIESRESISTOR * analog_value / (1023 - analog_value)) * (-1);