from threading import Thread
from influx_poster import database_post
from time import sleep, time
import datetime
import serial
import csv

port = '/dev/serial/by-id/usb-Texas_Instruments_CC1111_USB_CDC_000001-if00'
baud = 9600 
 
class SerialManager(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.last_reading = datetime.datetime.now() - datetime.timedelta(minutes=15)
        self.exit = 0
 
    def get_last_reading(self) :
        return self.last_reading

    def run(self):
        # TODO: if the last stop start is a start (i.e. stop is missing) then insert stop
        try: 
            ser = serial.Serial(port=port, baudrate=baud, timeout=2)
            sleep(0.2)
            while True:
                if(self.exit) :
                    break
                char = ser.read()
                if char == 'a':
                    llapmsg = 'a'
                    while len(llapmsg) < 12:
                        llapmsg += ser.read()
                    if llapmsg[1:3] == 'SH':
                        timestamp = datetime.datetime.now()
                        self.last_reading = timestamp
                        tag = llapmsg[3:7]
                        value = llapmsg[7:].replace('-','')
                        dbpost = database_post(tag, value, "monitor").start()
                        timestring = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        with open("/home/jzc/logs/shower.csv", "a") as csvfile: 
                            showerwriter = csv.writer(csvfile, delimiter=',')
                            showerwriter.writerow([timestring, tag, value])
                    else: 
                        pass
                else:
                    pass
        finally:
            ser.close()

    def endSerial(self):
        self.exit=1