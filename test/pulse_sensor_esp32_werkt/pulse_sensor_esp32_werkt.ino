#include <config.h>

void setup() {
  Serial.begin(9600);
  pinMode(0, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(analogRead(0));
  delay(10);
  
}
