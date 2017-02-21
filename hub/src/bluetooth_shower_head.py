from threading import Thread
from time import sleep, time
from influx_poster import database_post
import datetime
import csv
import subprocess
import sys
import os
import signal
 
class bluetoothManager_head(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.exit = 0
 
    def endBluetooth(self): 
        self.exit = 1
        print("ending shower head")

    def run(self):
        try:
            print("started shower head")
            count = 0
            process = subprocess.Popen("exec /usr/bin/gatttool -b D0:4A:18:99:9E:9F -t random --char-write-req -a 0x23 -n 0100 --listen", shell=True, stdout=subprocess.PIPE)
            count2 = 0
            output = ""
            for line in iter(process.stdout.readline, ''):
                if (count < 2): 
                    count = count + 1
                else:
                    if(count2 < 3):
                        output = output + line[36:].replace(" ", "").strip()
                        count2 = count2 + 1
                        
                    else:
                        count2 = 0
                        array1 = output.decode('hex').split('*')
                        array2 = [s for s in array1 if len(s) > 5]
                        for item in array2: 
                            tag = item[:2]
                            value = item[2:]
                            dbpost = database_post(tag, value)
                            dbpost.start()
                            timestamp = datetime.datetime.now()
                            timestring = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                            with open("/home/jzc/logs/shower_head.csv", "a") as csvfile: 
                                showerwriter = csv.writer(csvfile, delimiter=',')
                                showerwriter.writerow([timestring, tag, value])
                        
                if(self.exit) :
                    print("attempting exit")
                    process.kill()
                    raise Exception("bluetooth ended")
        except Exception as error :
            print(repr(error))

    