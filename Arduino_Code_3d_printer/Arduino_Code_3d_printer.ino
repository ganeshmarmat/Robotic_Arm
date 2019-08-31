/*
  Software serial multple serial test

 Receives from the hardware serial, sends to software serial.
 Receives from software serial, sends to hardware serial.

 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)

 Note:
 Not all pins on the Mega and Mega 2560 support change interrupts,
 so only the following can be used for RX:
 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69

 Not all pins on the Leonardo and Micro support change interrupts,
 so only the following can be used for RX:
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).

 created back in the mists of time
 modified 25 May 2012
 by Tom Igoe
 based on Mikal Hart's example

 This example code is in the public domain.

 */
#include <SoftwareSerial.h>

#include <Servo.h>

Servo myservoA;  // create servo object to control a servo
Servo myservoB;
Servo myservoC;
//constant
int pinA=3;
int pinB=9;
int pinC=13;
int Dval=200;
bool derror=false;
// twelve servo objects can be created on most boards

int pos = 0;
int wait=0;
String iData=""; 
int olda=0,oldb=0,oldc=0;
SoftwareSerial mySerial(10, 11); // RX, TX
String pin="";
String value="";
bool switchflag=false;
float a=0,b=0,c=0;
void setup() {
  // Open serial communications and wait for port to open:
 
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(pinA,OUTPUT);
  pinMode(pinB,OUTPUT);
  pinMode(pinC,OUTPUT);
   myservoA.attach(pinA);
    myservoB.attach(pinB);
    myservoC.attach(pinC);
}
void servoPulse (int servo, int angle)
{
int pwm = (angle*11) + 500;      // Convert angle to microseconds
 digitalWrite(servo, HIGH);
 delayMicroseconds(pwm);
 digitalWrite(servo, LOW);
 delay(50);                   // Refresh cycle of servo
}
  
void makeallaction()
{
  myservoA.attach(pinA);
    myservoB.attach(pinB);
    myservoC.attach(pinC);
  /*
  servoPulse(pinA,a);
  servoPulse(pinB,b);
  servoPulse(pinC,c);
  */
  myservoA.write(a);
  
  myservoB.write(b);
  
  myservoC.write(c);
  
   myservoA.detach();
    myservoB.detach();
    myservoC.detach();
    
  delay(Dval);
  mySerial.write("1");
  
  Serial.println("send 1");
  Serial.println(iData);
  iData="";
  Serial.println("a="+String(a)+"b="+String(b)+"c="+String(c));
}

void setdata()
{
  for(int i=0;i<iData.length();i++)
  {
    char s=iData[i];
    if(s==''||s=='⸮'){
      iData="";
      mySerial.write("0");
      return;
    }
   if(s=='\n')
     {
     
      makeallaction();
      //Serial.println("called");
      
    }
    if(s=='|')
    {

    //makeAction();
    /*Serial.print(pin);
    Serial.print("=");
    Serial.print(value);
    Serial.print(",");
    */
    int pin1=pin.toInt();
    
  float value1=value.toFloat();
  if(value1>180){
    derror=true;
  }
  if(pin1==pinA)
  {
    a=value1;
  }
  if(pin1==pinB)
  {
    b=value1;
  }
  if(pin1==pinC)
  {
    c=value1;
  }
  
      pin="";
      value="";
      switchflag=false;
    }else if(s=='=')
    {
      switchflag=true;
    }else
    {
      if(s>='0' and s<='9' || s=='.'){
      
      if(switchflag)
      {
       value+=s; 
      }else
      {
        pin+=s;
      }
      
      }else
      {
        derror=true;
      }
    }
  }
}

void loop() { // run over and over

  
  if (mySerial.available()) {
    char s= mySerial.read();
  iData+=s;
  if(s==' ')
  {
    Serial.println("Error");
        Serial.println(iData);
        mySerial.write("0");
        iData="";
  }
  if(s=='\n')
  {
    setdata();  }
    
  }
    else{
      //Serial.println("no data");
      delay(Dval);
      if(wait==5){
      mySerial.write("0");wait=0;
      }
      wait++;
    }
    
    
    //myservo.write(s.toInt());
  }
 


