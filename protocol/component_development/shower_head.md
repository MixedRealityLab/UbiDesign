# Shower Head Monitor

## Components

- 1 * Adafruit BLE feather
- 1 * Adafruit BNO055 9 axis orientation sensor
- M5 nut and bolt to secure case to shower head
- 22AWG hookup wire
- 1 * 500mah lipo battery
- 1 * JST 2 wire assembly

## Procedure

- Solder Feather SCL, SDA, GND and 3v Pins to matching pins on dafruit BNO055 9 axis orientation sensor using 22AWG single core wire
- join JST wire assembly to battery using NASA method and 3mm 3:1 heatshrink
- plug battery into feather and charge until orange light has gone out (5 hours max)
- load firmware (shower_head.ino) on to feather using arduino IDE
- place assembled shower head monitor into case and attach M5 nut and bold for securing 
