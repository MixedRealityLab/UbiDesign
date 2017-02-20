#include <SPI.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM9DS0.h>
  
Adafruit_LSM9DS0 lsm = Adafruit_LSM9DS0(1000);  // Use I2C, ID #1000

#if not defined (_VARIANT_ARDUINO_DUE_X_) && not defined (_VARIANT_ARDUINO_ZERO_)
  #include <SoftwareSerial.h>
#endif

#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"

#include "BluefruitConfig.h"

#define VBATPIN A9

#define FACTORYRESET_ENABLE         1
#define MINIMUM_FIRMWARE_VERSION    "0.6.6"
#define MODE_LED_BEHAVIOUR          "MODE"

Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

void error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}


void setup(void) 
{
  /* Initialise the sensor */
  lsm.begin(); 
  lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_2G);
  lsm.setupMag(lsm.LSM9DS0_MAGGAIN_2GAUSS);
  lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_245DPS);
  ble.begin(VERBOSE_MODE);
  ble.factoryReset();
  ble.echo(false);
  ble.info();
  ble.verbose(false);
  
}

int count = 10;

void loop(void) 
{  
  while (! ble.isConnected()) {
      delay(500);
  }
  
  
  ble.setMode(BLUEFRUIT_MODE_DATA); 
  /* Get a new sensor event */ 
  sensors_event_t accel, mag, gyro, temp;
  lsm.getEvent(&accel, &mag, &gyro, &temp);
  
  String dataString = "";
  dataString += "*ax"; 
  dataString += accel.acceleration.x;
  dataString += "*";  
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "*ay"; 
  dataString += accel.acceleration.y;
  dataString += "*";  
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "*az"; 
  dataString += accel.acceleration.z;
  dataString += "*";  
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "*mx"; 
  dataString += mag.magnetic.x;
  dataString += "*";  
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "my"; 
  dataString += mag.magnetic.y;
  dataString += "*"; 
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "mz"; 
  dataString += mag.magnetic.z;
  dataString += "*"; 
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "gx"; 
  dataString += gyro.gyro.x;
  dataString += "*"; 
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "gy"; 
  dataString += gyro.gyro.y;
  dataString += "*"; 
  if(ble.isConnected()) 
    ble.print(dataString);
  dataString = "";
  dataString += "gz"; 
  dataString += gyro.gyro.z;
  dataString += "*"; 
  if(ble.isConnected()) 
    ble.print(dataString);
    
  if(ble.isConnected())
  {
    if(count == 0) {
      count = 10;
      float measuredvbat = analogRead(VBATPIN);
      measuredvbat *= 2;    // we divided by 2, so multiply back
      measuredvbat *= 3.3;  // Multiply by 3.3V, our reference voltage
      measuredvbat /= 1024; // convert to voltage
      dataString = "";
      dataString += "ba"; 
      dataString += measuredvbat;
      dataString += "*"; 
      ble.print(dataString);
    }
    
  }

  delay(250);
  count --;
  

  
}