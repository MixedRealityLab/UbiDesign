import time
import serial

port = '/dev/serial/by-id/usb-Texas_Instruments_CC1111_USB_CDC_000001-if00'
baud = 9600
count = 5

ser = serial.Serial(port=port, baudrate=baud)

while(count):
	ser.write("aSHFLOW21.1-")
	ser.write("aSHTEMP21.1-")
	ser.write("aSHTOTA21.1-")
	time.sleep(1)
	count = count - 1
	print(count)

ser.close()