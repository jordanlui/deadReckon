#include <Time.h>
#include <TimeLib.h> // Read more at http://playground.arduino.cc/Code/Time
#include <ArduinoJson.h> // Believe this is source: https://github.com/bblanchon/ArduinoJson

const int numdigits = 6;
int packetCount = 0;
int frequency = 100; // Frequency in Hz
const int delayTime = (int)(1 / frequency * 1000); // Loop time in milliseconds. Cast to int to be safe.


void setup() {
  Serial.begin(115200);


}

// Open JSON buffer

void loop() {
  // put your main code here, to run repeatedly:
  packetCount++;
  time_t t = now();
  StaticJsonBuffer<300> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();  
//  root["setup"] = "imuonly";
  root["time"] = t; // print the current time in seconds since jan 1 1970
  root["packet"] = packetCount;
  
  JsonArray& acc = root.createNestedArray("acc");
  acc.add(-0.083, numdigits);  // 6 is the number of decimals to print
  acc.add(0.00177, numdigits);   // if not specified, 2 digits are printed
  acc.add(0.9185, numdigits);   // if not specified, 2 digits are printed

  JsonArray& gyro = root.createNestedArray("gyro");
  gyro.add(0.38147, numdigits);  // 6 is the number of decimals to print
  gyro.add(-0.34332, numdigits);   // if not specified, 2 digits are printed
  gyro.add(0.007629, numdigits);   // if not specified, 2 digits are printed

  JsonArray& mag = root.createNestedArray("mag");
  mag.add(-320.155, numdigits);  // 6 is the number of decimals to print
  mag.add(-39.5952, numdigits);   // if not specified, 2 digits are printed
  mag.add(-82.8297, numdigits);   // if not specified, 2 digits are printed

  root.printTo(Serial);
  // This prints:
  
  Serial.println();
//  root.prettyPrintTo(Serial); // could pretty print but we don't need this
  delay(delayTime);

}
