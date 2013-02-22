/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int red = 13;
int yel = 12;
int gre = 11;
int incomingByte = 0;
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(red, OUTPUT);
  pinMode(yel, OUTPUT);  
  pinMode(gre, OUTPUT);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte);
    if (incomingByte == 103) { // g = GREEN
        digitalWrite(red, LOW);
        digitalWrite(yel, LOW);
        digitalWrite(gre, HIGH);
    } else if (incomingByte == 121) { // y = YELLOW
      digitalWrite(red, LOW);   
      digitalWrite(yel, HIGH);
      digitalWrite(gre, LOW);
    } else if (incomingByte == 114) { // r = RED
      digitalWrite(red, HIGH);
      digitalWrite(yel, LOW);
      digitalWrite(gre, LOW);
    } else if (incomingByte == 48) { // 0 = NONE
      digitalWrite(red, LOW);
      digitalWrite(yel, LOW);
      digitalWrite(gre, LOW);
    }
  }

}
