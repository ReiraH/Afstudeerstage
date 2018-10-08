   #define RESISTOR 10000 //This should be the same value of the used resistor  
   #define RUBBERCORDPIN A0  //This is the pin where the cord is connected tp
   
   void setup(void) { 
     Serial.begin(9600); 
   } 
   
   void loop(void) { 
     int value; 
     value = analogRead(RUBBERCORDPIN);     //Read value
     Serial.print("Analog reading ");  
     Serial.println(value);                 //Print value
     delay(1000); 
   } 
