/*
 
 */
#include <SoftwareSerial.h>

#include <Servo.h>

//anlog input pin
#define inputA A0
#define inputB A1
#define inputC A2

Servo myservoA;  // create servo object to control a servo
Servo myservoB;
Servo myservoC;
//constant
int pinA=3;
int pinB=9;
int pinC=13;
int recordingButton=6;
int playingButton=7;
int Dval=100; //delay for all

bool derror=false;

int pos = 0;
int wait=0;
String iData=""; 
bool Recording=false;
bool Playing=false;
String RecordingData="";
SoftwareSerial mySerial(10, 11); // RX, TX
char pin=' ';
String value="";
bool switchflag=false;
float a=0,b=0,c=0;
void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(pinA,OUTPUT);
  pinMode(pinB,OUTPUT);
  pinMode(pinC,OUTPUT);
  pinMode(inputA,INPUT);
  pinMode(inputB,INPUT);
  pinMode(inputC,INPUT);
  pinMode(recordingButton,INPUT);
  pinMode(playingButton,INPUT);
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
 /* myservoA.attach(pinA);
    myservoB.attach(pinB);
    myservoC.attach(pinC);
 */ /*
  servoPulse(pinA,a);
  servoPulse(pinB,b);
  servoPulse(pinC,c);
  */
  myservoA.write(a);
  
  myservoB.write(b);
  
  myservoC.write(c);
  
   /*myservoA.detach();
    myservoB.detach();
    myservoC.detach();
    */
  delay(Dval/2);
  //mySerial.write("1");
  mySerial.flush();//flush buffer
  
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
    
    
  float value1=value.toFloat();
  if(value1>180){
    derror=true;
  }
  if(pin=='A')
  {
    a=value1;
  }
  if(pin=='B')
  {
    b=value1;
  }
  if(pin=='C')
  {
    c=value1;
  }
  
      pin=' ';
      value="";
      switchflag=false;
    }else if(s=='A'||s=='B'||s=='C')
    {
      pin=s;
      
      switchflag=true;
    }else
    {
      if(s>='0' and s<='9' || s=='.'){
      
      if(switchflag)
      {
       value+=s; 
      }
      
      }else
      {
        derror=true;
      }
    }
  }
}
void makeRecording()
{
 
    int na=analogRead(inputA);
    int nb=analogRead(inputB);
    int nc=analogRead(inputC);
    Serial.println("record na="+String(na)+",b="+String(nb)+",c="+String(nc));
    na=map(na, 107 , 491, 0, 180);
    nb=map(nb, 107 , 491, 0, 180);
    nc=map(nc, 107 , 491, 0, 180);
    Serial.println("record a="+String(a)+",b="+String(b)+",c="+String(c));
    bool isdatacatch=false;
    if(na!=a)
    {
      a=na;
      RecordingData+="A"+String(a)+"|";
      isdatacatch=true;
    }
    if(nb!=b)
    {
      b=nb;
      RecordingData+="B"+String(b)+"|";
      isdatacatch=true;
    }
    if(nc!=c)
    {
      c=nc;
      RecordingData+="C"+String(c)+"|";
      isdatacatch=true;
    }
    if(isdatacatch)
    {
      RecordingData+="\n";
    } 
   
    
    
}
void makePlay()
{
   for(unsigned long i=0;i<RecordingData.length();i++)
  {
  addtodata(RecordingData[i]);
  Serial.print(RecordingData[i]);
  }
}

void addtodata(char s)
{
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
    setdata();  
   }
}
void loop() { 
delay(Dval*2);
 Recording=digitalRead(recordingButton);
 delay(Dval*2);
 Recording=digitalRead(recordingButton);

if(Recording)
{
  myservoA.detach();
  myservoB.detach();
  myservoC.detach();
  delay(Dval*2);
  RecordingData="";
  delay(Dval);
}
  while(Recording)
  {Recording=digitalRead(recordingButton);
    Serial.println("Recording");
    makeRecording();
    delay(Dval);
  }

  Playing=digitalRead(playingButton);
if(Playing)
{
  myservoA.attach(pinA);
    myservoB.attach(pinB);
    myservoC.attach(pinC);
    delay(Dval*2);
  Serial.println(RecordingData);
   
 Serial.println("playinging");
}
  while(Playing){
 Playing=digitalRead(playingButton);
 makePlay();  
 delay(Dval);
  }
 
 
  if (mySerial.available())
  {
    char s= mySerial.read();
    addtodata(s);
    
  }
   else
    {
      //Serial.println("no data");
      delay(Dval);
      if(wait==5)
      {
        mySerial.write("0");
        mySerial.flush();//clear buffer
        wait=0;
      }
      wait++;
    }
    
  
    //myservo.write(s.toInt());
  }
 


