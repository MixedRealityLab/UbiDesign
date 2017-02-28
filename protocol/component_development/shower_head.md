# Shower Head Monitor

## Components

- 1 * Adafruit BLE feather
- 1 * Adafruit BNO055 9 axis orientation sensor
- M5 nut and bolt to secure case to shower head
- 22AWG hookup wire
- 1 * 500mah lipo battery
- 1 * JST 2 wire assembly

## Build Procedure

- Solder Feather SCL, SDA, GND and 3v Pins to matching pins on dafruit BNO055 9 axis orientation sensor using 22AWG single core wire
- join JST wire assembly to battery using NASA method and 3mm 3:1 heatshrink
- plug battery into feather and charge until orange light has gone out (5 hours max)
- load firmware (shower_head.ino) on to feather using arduino IDE
- place assembled shower head monitor into case and attach M5 nut and bold for securing 

## Testing

SSH into the hub and run
``` 
sudo python test_shower_head.py 

```
move the shower head around for 10 seconds then connect to the hub using a web browser on port 8083, select the shower database and query for recent readings

## Commissioning
- Fully charge battery until orange light has gone out
- Place board assebly and battery into container
- fix container to shower head using built in clip and m5 nut and bolt
