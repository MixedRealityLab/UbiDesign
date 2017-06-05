import time
import serial
import csv
import sys

filename = str(sys.argv[1])

port = '/dev/tty.usbmodem000001'
baud = 9600
ser = serial.Serial(port=port, baudrate=baud)


with open(filename, 'rU') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		forsend = "aSHFLOW" + str(row[1])
		ser.write(forsend.ljust(12,'-'))
		
		forsend = "aSHTEMP" + str(row[2])
                ser.write(forsend.ljust(12,'-'))
		time.sleep(1)

ser.close()
