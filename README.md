# UbiDesign Shower Study
This repo contains the resources required to construc the hardware and software required to deploy the UbiDesign shower study kit. It is currently under development and as such may drastically change

The kit is designed as a technology probe to investigate the potential utility of IoT shower data in the design manufacturing process as part of the UbiDesign Project - <http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/N005945/1>

It consists of:
* A BLE shower products shelf
* A BLE shower head movement tracker
* A RF flow and temperature monitor
* A hub which collects, stores and makes available the data collected by the above sensors

## BLE shower products shelf

### Hardware components
* BLE Feather micro controller board
* HX711 Amplifier and ADC boards
* 500g rated load cells
* 3.7v LiPo single cell batteries

### 3D Design files
* The AutoDesk design and STL files for the battery encolsure and shelf plates can be found within this repository

### Firmware
* Firmware is built to run on an ATMEGA328 µProcessor and can be flashed using either the Arduino IDE or AVR Dude tool

### Electronics Schematic
* The Eagle cad schematics file can be found within this repository

## BLE shower head movement tracker

### Hardware components
* Metawear R Pro BLE accelerometer and gyro
* 500mah LiPo single cell battery

## RF flow and temperature monitor

### Hardware components
* Wireless Things RFµ328 all in one board
* Flow sensor
* Hyrdo electric mini generator
* Temperature sensor
* 3.3v two way voltage regulator

### Firmware
* Firmware is built to run on an ATMEGA328 µProcessor and can be flashed using either the Arduino IDE or AVR Dude tool

### Electronics Schematic
* The Eagle cad schematics file can be found within this repository

## Hub

### Hardware
* Raspberry Pi 3 + Power Supply + 8GB SD card
* Wireless things radio module (USB or GPIO Serial)

### Sofware modules
The below software modules can be found within this repository
* Shower flow and temperature monitor - a node application which listens on the serial port for readings from the RFµ328
* BLE monitor app - a node application which watches the local InfluxDB to detect the start and end of showers and conneted to the BLE peripherials when the shower is active









