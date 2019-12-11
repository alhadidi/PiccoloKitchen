//INCLUDE LIBRARIES NEEDED
#include <Servo.h>

//SET CONSTANTS AND PINS
//PIN SETUP
const int servoPin = 8;
const int motorPin = 7;
const int upper_LS_PIN = 10;
const int lower_LS_PIN = 11;
const int up_but = 4;
const int d_but = 5;
//SERVO SETUP
Servo myservo; 
const int RAT_RELEASE = 70;
const int RAT_ENGAGE = 100;
int up_val;
int d_val;
//MOTOR SETUP
Servo motor;

void setup() {
  // put your setup code here, to run once:
  //PIN MODES
  pinMode(servoPin, OUTPUT);
  pinMode(upper_LS_PIN, INPUT_PULLUP);        //These need pullup resistors due to how their wired
  pinMode(lower_LS_PIN, INPUT_PULLUP);
  pinMode(up_but, INPUT);
  pinMode(d_but, INPUT);
  //PIN ATTACHMENTS
  myservo.attach(servoPin);
  motor.attach(motorPin);
  //ENABLE SERVO AND MOTOR
  cabinet_stall();
  engage_ratchet();


  //_________________________TEST_CODE______________________________________________
  
  
}

void loop() {
  // put your main code here, to run repeatedly:
  up_val = digitalRead(up_but);
  d_val = digitalRead(d_but);
  if(up_val==HIGH && d_val==LOW){
    cabinet_up_activate();
  }
  else if(up_val==LOW && d_val==HIGH){
    cabinet_down_activate();
  }
  else {
    cabinet_stall();
  }
}


/*FUNCTIONS LIST
 * The following are functions written to make the above code much easier
 * to understand and much more usable.
 */

 /*
  * NOTE: This function releases the ratchet and then drives it in the down
  * position indefinetly, ensure the cabinet is stopped at some point.
  */
void cabinet_down() {
  motor.writeMicroseconds(1400); //Take Load off Ratchet 
  delay(250); //WAIT for the weight to be taken off
  disengage_ratchet(); //RELEASE the Ratchet
  delay(100); //Allow time for the Ratchet to release 
  motor.writeMicroseconds(1750); //Drive the cabinet DOWN
}

 /*
  * NOTE: This function drives it in the up
  * position indefinetly, ensure the cabinet
  * is stopped at some point.
  */
void cabinet_up() {
  motor.writeMicroseconds(1350);
}

 /*
  * NOTE: This function sets the motor to the STOPPED or center value.
  */
void cabinet_stall() {
  motor.writeMicroseconds(1500);
}

 /*
  * NOTE: Engages the ratchet.
  */
void engage_ratchet() {
  myservo.write(RAT_ENGAGE);
}

 /*
  * NOTE: Disengages the ratchet.
  */
void disengage_ratchet() {
  myservo.write(RAT_RELEASE);
}

void cabinet_down_activate() {
  int a = digitalRead(upper_LS_PIN);
  int b = digitalRead(lower_LS_PIN);
  cabinet_down();     //first we tell the cabinet to go down
  while(b == HIGH){
    a = digitalRead(upper_LS_PIN);
    b = digitalRead(lower_LS_PIN);
    //do nothing
    //when this changes we move on to stop cabinet
  }
  cabinet_stall();    //Move to slow-close
  delay(200);
  engage_ratchet();
}

void cabinet_up_activate() {
  int a = digitalRead(upper_LS_PIN);
  int b = digitalRead(lower_LS_PIN);
  cabinet_up();        //Move the cabinet UP
  while(a == HIGH){
    a = digitalRead(upper_LS_PIN);
    b = digitalRead(lower_LS_PIN);
    //do nothing
    //when this changes we move on to stop cabinet
  }
  cabinet_stall();    //Stop the cabinet 
}
