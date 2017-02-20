
/* Complete code for the "smart shower" */

#include <Arduino.h>
#include <LLAPSerial.h>
#include <OneWire.h>
#include <DallasTemperature.h>

//Defines
#define HUBID "SH"      // this is the LLAP Hub ID
#define RADIO_PIN 8

// Function declarations
void getFlowData();
void getTempData();
void resetFlowData();
void calcFlow();
void pulseCounter();
boolean fcnSend(String,String);
boolean fcnSend(String,int);
boolean fcnSend(String,double);
boolean fcnSend(String,float);
void toggleValve();

//The Hall-effect sensor is connected to pin 2 which uses interrupt 0
#define calibrationFactor 6.8
#define FLOW_SENSOR_PIN  2
#define FLOW_SENSOR_INTERRUPT_PIN  0
#define refreshRate  1000
String pulseCountString;
volatile int pulseCount=0;
int pc = 0;
float totalFlow = 0, flowRate = 0;
// oldTime is actual timestep between flow calculations (defined by flow)
// lastTime is defined by the processor
unsigned long dt, oldTime, lastTime;
void flowSensorSetup(){
  oldTime = millis();
  pinMode(FLOW_SENSOR_PIN, INPUT);
  digitalWrite(FLOW_SENSOR_PIN, HIGH);
  pinMode(FLOW_SENSOR_INTERRUPT_PIN, INPUT);
  attachInterrupt(FLOW_SENSOR_INTERRUPT_PIN, pulseCounter, FALLING);
}

// DS18S20 Temperature chip connected to pin 3
OneWire oneWire(3);
DallasTemperature tempSensor(&oneWire);
float tempData;

// Other analogue input pins (battery and generator sensing)
float sensitivity = 4.1/1024;   // regulator outputs 4.1V
int batterySensorPin = 2;
float batteryVoltage;
int generatorSensorPin = 1;
float generatorVoltage;
// Potential divider to scale down battery voltage
float R1 = 10000;
float R2 = 10000;
float batteryScale = (R1+R2)/R2;

int status;

// set value that an analog pin input must be before it is defined as high
int high = 3.2/0.005;  // Anything above source voltage is set as high
long time = 0;
long debounce = 500;    // added time to allow button to be re-pressed


void radioSetup(){
  pinMode(RADIO_PIN, OUTPUT);   // initialize pin 8 to control the radio
  digitalWrite(RADIO_PIN, HIGH); // select the radio
  Serial.begin(115200);  // start the serial port at 115200 baud
  delay(1000);           // allow the radio to startup
  //give device ID
  LLAP.init("SH");
  Serial.println("STARTED");
  Serial.flush();
}

void setup(){
  radioSetup();
  flowSensorSetup();
  tempSensor.begin();
  lastTime = millis();
}

void loop(){
  getFlowData();
  getTempData();
  generatorVoltage = analogRead(generatorSensorPin) * sensitivity;
  batteryVoltage = analogRead(batterySensorPin) * batteryScale * sensitivity;
  if (millis()-lastTime >= refreshRate){
    fcnSend("FLOW",flowRate);
    fcnSend("TOTA",totalFlow);
    fcnSend("TEMP",tempData);
    resetFlowData();
    lastTime=millis();
  }
}

//receive message


void getFlowData(){
    dt = millis() - oldTime;
    if ((pulseCount != 0) && (dt >= refreshRate)){
        calcFlow();
    }
}

void getTempData(){
  tempSensor.requestTemperatures();
  tempData = tempSensor.getTempCByIndex(0);
}

void resetFlowData(){
    pc = 0;
    flowRate = 0;
}

void calcFlow(){
  // Disable water flow interrupt
  detachInterrupt (FLOW_SENSOR_INTERRUPT_PIN);
  // Reset variables
  pc = pulseCount;
  pulseCount = 0;
  // re-enable interrupt
  attachInterrupt(FLOW_SENSOR_INTERRUPT_PIN, pulseCounter, FALLING);

  flowRate = (1000 / refreshRate) * (pc / calibrationFactor);
  //update total
  totalFlow += flowRate * (float)refreshRate / 1000.0 / 60.0;
}

void pulseCounter(){
    if (pulseCount==0)
        oldTime = millis();
    pulseCount++;
}

boolean fcnSend(String command,String value){
  //takes in recipiant ID and the Message
  String message = command+value;
  if(message.length()<=9){
    // message is needed to be less than 9 characters
    String command = "a";
    int messageLength = 1;
    command.concat(HUBID);
    //required to be upper case so can be seen
    message.toUpperCase();
    command.concat(message);
    messageLength = command.length();
    //add padding
    while(messageLength <12){
      command.concat("-");
      messageLength = command.length();
    }
    Serial.println(command);
    //return true meaning the message was created okay
    return true;
  } else {
    //return true meaning the message was too long
    fcnSend(command,value.substring(0,4));
    return false;
  }
}

boolean fcnSend(String command,int value){
    return fcnSend(command,String(value));
}
boolean fcnSend(String command,double value){
    return fcnSend(command,String(value));
}
boolean fcnSend(String command,float value){
    return fcnSend(command,String(value));
}


