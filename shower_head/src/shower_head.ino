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
#define BNO055_SAMPLERATE_DELAY_MS (100)

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

volatile bool watchdogActivated = false;

ISR(WDT_vect)
{
  // Set the watchdog activated flag.
  watchdogActivated = true;
}

void sleep()
{
  // Set sleep to full power down.  Only external interrupts or 
  // the watchdog timer can wake the CPU!
  set_sleep_mode(SLEEP_MODE_PWR_DOWN);

  // Turn off the ADC while asleep.
  power_adc_disable();

  // Enable sleep and enter sleep mode.
  sleep_mode();

  // CPU is now asleep and program execution completely halts!
  // Once awake, execution will resume at this point.
  
  // When awake, disable sleep mode and turn on all devices.
  sleep_disable();
  power_all_enable();
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

  noInterrupts();
  
  // Set the watchdog reset bit in the MCU status register to 0.
  MCUSR &= ~(1<<WDRF);
  
  // Set WDCE and WDE bits in the watchdog control register.
  WDTCSR |= (1<<WDCE) | (1<<WDE);

  // Set watchdog clock prescaler bits to a value of 8 seconds.
  WDTCSR = (1<<WDP0) | (1<<WDP3);
  
  // Enable watchdog as interrupt only (no reset).
  WDTCSR |= (1<<WDIE);
  
  // Enable interrupts again.
  interrupts();

  

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
      imu::Vector<3> gyr = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);

      if(ble.isConnected()) 
        ble.print('a' + String(acc.x()) + ',' + String(acc.y()) + ',' + String(acc.z()) + '*');
        ble.print('g' + String(gyr.x()) + ',' + String(gyr.y()) + ',' + String(gyr.z()) + '*');
        ble.print('m' + String(mag.x()) + ',' + String(mag.y()) + ',' + String(mag.z()) + '*'); 
       
        
      delay(BNO055_SAMPLERATE_DELAY_MS);
      
  }
  Serial.print("checking to sleep");
  if(!ble.isConnected()) {
      Serial.print("Going to sleep");
      delay(200);
      sleep();
  }






}