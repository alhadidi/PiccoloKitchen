//Configure pins
int pulsepin=3;
int highpin=2;
int medpin=7;
int lowpin=8;
int reversepin=12;
int fsr1pin=0;

//Leadscrew mechanical config
int pos[]={0, 360, 820}; //Bottom, middle and top positions in mm
int resolution=1600; //steps per revolution
int prevpos = pos[0]; //Arduino will consider the starting position is the lowest: be carefull at reboot
int lead=10; //mm per revolution

//Trapezoid aceleration profile config
int accelgaps=25; //Gaps between speed 0 and speed max
int acceltime=1000; //The accelgaps will be distributed along 1000ms in "slots"
float slottime=acceltime/accelgaps;
float vmax=60; //Max speed is 60mm/s
int realaccelgaps; //Not always will do all of them, if the path is shorter
float realvmax; //If not all accelgaps are done, real vmax will not be vmax
float freq;

//Error correction config
int errorreversedist=10; //if an error is found, it will go back 10mm
int errorreverseconst=10; // speed when reversed will be vmax/k until 10mm are covered

//Other calculations: conversion constants
float mmtostep=resolution/lead;
float maxfreq=vmax*mmtostep;

void setup() {
  //Configure button pins
  pinMode(highpin, INPUT_PULLUP);
  pinMode(medpin, INPUT_PULLUP);
  pinMode(lowpin, INPUT_PULLUP);

  //Configure FSR pin
  pinMode(fsr1pin,INPUT);

  //Configure driver outputs
  pinMode(pulsepin, OUTPUT);
  pinMode(reversepin, OUTPUT);

  //Start Serial monitor communications
  Serial.begin(9600); 
}

void loop() {
  Serial.print("prevpos: "); Serial.println(prevpos);

  // When a button is pressed it is checked if there is an error (custom function) and if the previous position is the one we are aiming for:
  //If it is not, the cabinet moves (another sample function)
  if (digitalRead(highpin)==0 and checkerror()==false){
    if (prevpos!=pos[2]){prevpos=movecabinet(prevpos,pos[2]);}
  }
  else if (digitalRead(medpin)==0 and checkerror()==false){
    if (prevpos!=pos[1]){prevpos=movecabinet(prevpos,pos[1]);}
  }
  else if (digitalRead(lowpin)==0 and checkerror()==false){
    if (prevpos!=pos[0]){ prevpos=movecabinet(prevpos,pos[0]);}
  }

  //Delay 100ms
  delay(100);
}

int movecabinet(int startpos, int finishpos){

  bool error=false;

  //Set movement direction
  setdirection(startpos,finishpos);

  //Calculate total steps to be done and step counter initialization
  long totalsteps=convertmmtostep(finishpos-startpos);
  unsigned long absolutetotalsteps=abs(totalsteps);
  float aggsteps=0;
  float currentsteps=0;

  Serial.print("\n\n*************START!!*************** "); Serial.print(startpos); Serial.print(", "); Serial.print(finishpos); Serial.print(", "); Serial.print(totalsteps); Serial.print(", "); Serial.println(absolutetotalsteps); 

  //Computation to check if all steps will be taken and if realvmax will be vmax
  for (float i=1;i<=accelgaps; i++){
      freq=convertspeedtofreq(vmax,i/accelgaps);
      currentsteps=calculatesteps(freq,slottime);
      aggsteps=aggsteps+currentsteps;  
  }
  int maxaccelsteps=aggsteps;
  if (absolutetotalsteps>2*maxaccelsteps){realaccelgaps=accelgaps; realvmax=vmax; /*Serial.println("Normal")*/;}
  else {
      float count=0;
      float newaccelsteps=0;
      while (newaccelsteps*2<absolutetotalsteps){
          count=count+1;
          freq=convertspeedtofreq(vmax,count/accelgaps);
          currentsteps=calculatesteps(freq,slottime);
          newaccelsteps=newaccelsteps+currentsteps;
      }
      
      realaccelgaps=count-1;
      realvmax=vmax*realaccelgaps/accelgaps;

      //Serial.println("Weird");
  } 

  // Computation done: aggsteps back to 0
  aggsteps=0;

  //Movement starts
  //Movement: Acceleration stage
  for (float i=1;i<=realaccelgaps; i++){
      if (error==false){
          unsigned long rstime=millis();

          freq=convertspeedtofreq(realvmax,i/realaccelgaps);
          tone (pulsepin,freq); //Sets a specific frequency in a pin. Higher freqs=faster movemnt
          
          currentsteps=calculatesteps(freq,slottime); //Calculate steps at this acceleration stage
          aggsteps=aggsteps+currentsteps;
          
          unsigned long timetodelay=slottime+rstime-millis(); //While the slottime passes, it constantly checks is there is any error
          
          while(timetodelay>(millis()-rstime) and error==false){
              error=checkerror();
              if (error!=false){break;}
          }
      }
      else{break;}
  }

  //Serial.print("\tST1: aggsteps: "); Serial.print(aggsteps); Serial.print("; aggmm: "); Serial.println(convertsteptomm(aggsteps));

  //Movement: Constant speed stage
  float constantspeedsteps;
  float constantspeedtime;
  
  if (error==false){
      unsigned long rstime=millis();
      
      constantspeedsteps=absolutetotalsteps-2*aggsteps;
      constantspeedtime=constantspeedsteps/freq*1000; //in milliseconds
    
      //Serial.print("\n\tconstantspeedsteps"); Serial.print(", ");Serial.print(constantspeedsteps); Serial.print("; "); Serial.println(constantspeedtime);
       
      tone (pulsepin, freq); 
      unsigned long tonestart=millis();
      
      while(constantspeedtime>millis()-rstime and error==false){
          error=checkerror();
          if (error!=false){break;}
      }
      
      currentsteps=calculatesteps(freq,millis()-tonestart); //revisar si hay que meter adentro
      aggsteps=aggsteps+currentsteps;
  }
  
  //Serial.print("\tST2: aggsteps: "); Serial.print(aggsteps); Serial.print("; aggmm: "); Serial.println(convertsteptomm(aggsteps));
  
  //Movement: Decceleration stage  
  for (float i=1;i<=realaccelgaps; i++){
      if (error==false){
          unsigned long rstime=millis();

          freq=convertspeedtofreq(realvmax,(realaccelgaps+1-i)/realaccelgaps);
          tone (pulsepin, freq);
          
          currentsteps=calculatesteps(freq,slottime);          
          aggsteps=aggsteps+currentsteps;
    
          unsigned long timetodelay=slottime+rstime-millis();
    
          while(timetodelay>millis()-rstime and error==false){
              error=checkerror();
              if (error!=false){break;}
          }
      }
      else{break;}
  }

  //Serial.print("\tST3: aggsteps: "); Serial.print(aggsteps); Serial.print("; aggmm: "); Serial.println(convertsteptomm(aggsteps));
  
  if (error!=false){
      noTone (pulsepin); //Notone is necesary to stop high low square waves
      delay(100);
      setdirectionreverse(startpos,finishpos);

      float reversefreq=maxfreq/errorreverseconst;
      
      
      tone (pulsepin, reversefreq);
        
      float reversetimetodelay=min(errorreversedist,convertsteptomm(aggsteps))*resolution/reversefreq/lead*1000;
      
      delay(reversetimetodelay);
      aggsteps=aggsteps-reversetimetodelay/1000*reversefreq;
      
  }

  //Serial.print("\tST4: aggsteps: "); Serial.print(aggsteps); Serial.print("; aggmm: "); Serial.println(convertsteptomm(aggsteps));

  //Set no tone
  noTone (pulsepin);

  if (finishpos<startpos){ return (startpos-convertsteptomm(aggsteps));}
  else {return (startpos+convertsteptomm(aggsteps)); }
}

bool checkerror(){
  if (analogRead(fsr1pin)<600){return true;}
  else {return false;}
}

void setdirection(int startpos, int finishpos){
  if (finishpos<startpos){ digitalWrite(reversepin, LOW);}
  else {digitalWrite(reversepin, HIGH); } 
}

void setdirectionreverse(int startpos, int finishpos){
  if (finishpos<startpos){ digitalWrite(reversepin, HIGH);}
  else {digitalWrite(reversepin, LOW); } 
}

float convertsteptomm(float stepvalue){
  return (stepvalue/mmtostep);
}

float convertmmtostep(float mmvalue){
  return (mmvalue*mmtostep);
}

float convertspeedtofreq (float vel, float coef){
  return (vel*coef*mmtostep);
}

float calculatesteps(float freq, float tmiliseconds){
  return (freq*tmiliseconds/1000);
}

