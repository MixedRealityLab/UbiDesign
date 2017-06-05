#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <avr/sleep.h>
#include <avr/power.h>
#include <avr/wdt.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"
#include "BluefruitConfig.h"

#define VBATPIN A9
#define FACTORYRESET_ENABLE         1
#define MINIMUM_FIRMWARE_VERSION    "0.6.6"
#define MODE_LED_BEHAVIOUR          "MODE"
#define BNO055_SAMPLERATE_DELAY_MS (400)

Adafruit_BNO055 bno = Adafruit_BNO055();

#if not defined (_VARIANT_ARDUINO_DUE_X_) && not defined (_VARIANT_ARDUINO_ZERO_)
  #include <SoftwareSerial.h>
#endif

Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

void error(const __FlashStringHelper*err) 
{
  Serial.println(err);
  while (1);
}





void setup(void)
{
  Serial.begin(9600);
  
  if(!bno.begin())
  {
    Serial.print("wiring failure");
    while(1);
  }

  delay(500);

  ble.begin(VERBOSE_MODE);
  ble.factoryReset();
  ble.echo(false);
  ble.info();
  ble.verbose(false);
  delay(1000);
}


void loop(void)
{

    Serial.print("waiting for BLE");
  if(! ble.isConnected()) {
      delay(10000);
  }
  Serial.print("Passed Waiting");

  if(ble.isConnected()) {
      ble.setMode(BLUEFRUIT_MODE_DATA); 
      /* Get a new sensor event */ 
      imu::Vector<3> acc = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
      imu::Vector<3> mag = bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);
      //imu::Vector<3> gyr = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);

      if(ble.isConnected()) 
        ble.print('a' + String(acc.x()) + ',' + String(acc.y()) + ',' + String(acc.z()) + '*');
        delay(80);
        //ble.print('g' + String(gyr.x()) + ',' + String(gyr.y()) + ',' + String(gyr.z()) + '*');
        //delay(60);
        ble.print('m' + String(mag.x()) + ',' + String(mag.y()) + ',' + String(mag.z()) + '*'); 
        delay(80);
       
        
      delay(BNO055_SAMPLERATE_DELAY_MS);
      
  }
  Serial.print("checking to sleep");
  if(!ble.isConnected()) {
      Serial.print("Going to sleep");
      delay(200);
  }






}