//**************************************************************************//
//**************************************************************************//
//                     Front cabinet mechanism - SW                         //
//                       Borja Apaolaza Emparanza                           //
//                               May 2019                                   //
//                             MIT Media Lab                                //
//**************************************************************************//
//**************************************************************************//
               

//Up and down limit switch pins
const int uppin=2;
const int downpin=3;

//Up and down button pins
const int ubpin=8;
const int dbpin=9;

//Relay pins
const int r1pin=12;
const int r2pin=13;

// Initialize limit switches' values as HIGH
int upvalue=HIGH;
int downvalue=HIGH;

// Initialize button states
int ubvalue;
int dbvalue;


void setup() {
  // Button's modes are pullup input(LOW if pressed)
  pinMode(ubpin, INPUT_PULLUP);
  pinMode(dbpin, INPUT_PULLUP);

  // Switches' modes are pullup input
  pinMode(uppin, INPUT_PULLUP);
  pinMode(downpin, INPUT_PULLUP);

  // Relay pins' modes are output
  pinMode(r1pin, OUTPUT);
  pinMode(r2pin, OUTPUT);

  // Relays will start at HIGH
  digitalWrite(r1pin,HIGH);
  digitalWrite(r2pin, HIGH);
}

void loop() {
  // Read input from buttons
  ubvalue=digitalRead(ubpin);
  dbvalue=digitalRead(dbpin);

  //Read input from limit switches
  upvalue=digitalRead(uppin);
  downvalue=digitalRead(downpin);
  
  if (ubvalue==LOW){
      while (upvalue==HIGH){
           // If upper button is pressed, while the upper limit switch is not pressed, direct polarity is activated
           digitalWrite(r1pin,HIGH);
           digitalWrite(r2pin, LOW);

           // Per turn, the switch's state is checked
           upvalue=digitalRead(uppin);
      }
  }
  else if (dbvalue==LOW){
      while (downvalue==HIGH){
           // This case is analogous and inverse to the previous one
           digitalWrite(r1pin,LOW);
           digitalWrite(r2pin, HIGH);
           
           downvalue=digitalRead(downpin);
      } 
  }
  else{
      // If none of the buttons is pressed, no polarity at the motor.
      digitalWrite(r1pin,HIGH);
      digitalWrite(r2pin, HIGH);
  }

  // Delay 100ms
  delay (100);
}
