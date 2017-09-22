#include <Time.h>
#include <TimeLib.h> // Read more at http://playground.arduino.cc/Code/Time
#include <ArduinoJson.h> // Believe this is source: https://github.com/bblanchon/ArduinoJson

int numdigits = 6;
void setup() {
  Serial.begin(9600);


}

// Open JSON buffer



void loop() {
  // put your main code here, to run repeatedly:
  time_t t = now();
  StaticJsonBuffer<300> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();  
  root["setup"] = "imuonly";
  root["time"] = t; // print the current time in seconds since jan 1 1970
  
  JsonArray& acc = root.createNestedArray("acc");
  acc.add(48.756080, numdigits);  // 6 is the number of decimals to print
  acc.add(-11.72221223, numdigits);   // if not specified, 2 digits are printed
  acc.add(201.20202020, numdigits);   // if not specified, 2 digits are printed

  JsonArray& gyro = root.createNestedArray("gyro");
  gyro.add(38.756080, numdigits);  // 6 is the number of decimals to print
  gyro.add(-21.72221223, numdigits);   // if not specified, 2 digits are printed
  gyro.add(101.20202020, numdigits);   // if not specified, 2 digits are printed

  JsonArray& mag = root.createNestedArray("mag");
  mag.add(28.756080, numdigits);  // 6 is the number of decimals to print
  mag.add(-41.72221223, numdigits);   // if not specified, 2 digits are printed
  mag.add(78.20202020, numdigits);   // if not specified, 2 digits are printed

  root.printTo(Serial);
  // This prints:
  
  Serial.println();
//  root.prettyPrintTo(Serial); // could pretty print but we don't need this
  delay(200);

}
