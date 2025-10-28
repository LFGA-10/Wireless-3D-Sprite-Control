#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11); // RX, TX
const int VRx = A0;
const int VRy = A1;
const int SW = 2;

int lastX = 0;
int lastY = 0;

void setup() {
  pinMode(SW, INPUT_PULLUP);
  Serial.begin(9600);
  BT.begin(9600);
}

void loop() {
  int rawX = analogRead(VRx);
  int rawY = analogRead(VRy);
  int button = digitalRead(SW);

  lastX = (lastX * 0.8) + (rawX * 0.2);
  lastY = (lastY * 0.8) + (rawY * 0.2);

  BT.print("SANDRA:");
  BT.print((int)lastX);
  BT.print(",");
  BT.print((int)lastY);
  BT.print(",");
  BT.println(button);

  delay(80);
}
