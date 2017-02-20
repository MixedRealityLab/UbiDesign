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
* BLE UART Friend
* Sparkfun Open Scale
* 500g rated load cells
* 3.7v LiPo , 4400mah batteyr
* 5v Boost charger 

### 3D Design files
* The AutoDesk design and STL files for the battery encolsure and shelf plates can be found within this repository

### Firmware
* Uses stock Open Scale firmware

### Electronics Schematic
* Schematics can be seen on the Open Scale github repo

## BLE shower head movement tracker

### Hardware components
* Adafruit BLE Feather
* 500mah LiPo single cell battery
* Adafruit LSM9SO bord

The baords are connected via SPI interface

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
* The schematics file can be found within this repository

## Hub

### Hardware
* Raspberry Pi 3 + Power Supply + 8GB SD card
* Wireless things radio module (USB or GPIO Serial)

### Sofware 
Code is written in python with the following files

* main.py - has main control loop, initiating serial connection to WT serial adapeter. starts and stops shower head / scale threads when readings from WT serial adapter are received.
* bluetooth_scale.py - connects the the scale and reads data over BLE using gatt subprocess, data is inserted into influx
* bluetooth_shower_head.py - connects the the shower head sensor and reads data over BLE using gatt subprocess, data is inserted into influx
* influx_poster.py - short thread to make post to infuxdb
* wireless_things.py - connects to serial port and records wireless things shower monitor data
* sim.py - can be run on another pi with a wireless things adapter to simulate readings from the shower hub
* shower.service - systemctl service file, run directory should be modified to point to main.py source file

You will need to install influxdb ARM variant onto the pi along with the pyserial and influxdb python libraries











