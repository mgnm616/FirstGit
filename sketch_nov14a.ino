#include <Temperature_LM75_Derived.h>

Generic_LM75 LM75;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  delay(100);
}

void loop() {
  Serial.print(LM75.readTemperatureC());
  Serial.println(" C");

  delay(10);
}