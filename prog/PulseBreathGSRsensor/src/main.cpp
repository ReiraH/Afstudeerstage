#include <Arduino.h>
#include <ArduinoJson.h>

#define ANALOG_PIN_1 0
int analog_value = 0;

/*void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Analog IN Test");
}

void loop() {
  // put your main code here, to run repeatedly:
  analog_value = analogRead(ANALOG_PIN_1);
  Serial.println(analog_value);
  delay(500);
  
}*/

// ArduinoJson - arduinojson.org
// Copyright Benoit Blanchon 2014-2018
// MIT License



void setup() {
  // Initialize Serial port
  Serial.begin(115200);
  //while (!Serial) continue;
}

void loop() {
  // not used in this example

  // Memory pool for JSON object tree.
  //
  // Inside the brackets, 200 is the size of the pool in bytes.
  // Don't forget to change this value to match your JSON document.
  // Use arduinojson.org/assistant to compute the capacity.
  StaticJsonBuffer<200> jsonBuffer;

  // StaticJsonBuffer allocates memory on the stack, it can be
  // replaced by DynamicJsonBuffer which allocates in the heap.
  //
  // DynamicJsonBuffer  jsonBuffer(200);

  // Create the root of the object tree.
  //
  // It's a reference to the JsonObject, the actual bytes are inside the
  // JsonBuffer with all the other nodes of the object tree.
  // Memory is freed when jsonBuffer goes out of scope.
  JsonObject& root = jsonBuffer.createObject();
  
  // Add values in the object
  //
  // Most of the time, you can rely on the implicit casts.
  // In other case, you can do root.set<long>("time", 1351824120);
  analog_value = analogRead(ANALOG_PIN_1);
  root["sensor"] = "pulse sensor";

  // Add a nested array.
  //
  // It's also possible to create the array separately and add it to the
  // JsonObject but it's less efficient.
  JsonArray& data = root.createNestedArray("data");
  data.add(analog_value);
  //data.add(0022);

  root.printTo(Serial);
  // This prints:
  // {"sensor":"gps","time":1351824120,"data":[48.756080,2.302038]}

  Serial.println();

  //root.prettyPrintTo(Serial);
   delay(500);
  // This prints:
  // {
  //   "sensor": "gps",
  //   "time": 1351824120,
  //   "data": [
  //     48.756080,
  //     2.302038
  //   ]
  // }

    // put your main code here, to run repeatedly:
  /*analog_value = analogRead(ANALOG_PIN_1);
  Serial.println(analog_value);
  delay(500);*/
}