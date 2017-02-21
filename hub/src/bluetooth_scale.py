from __future__ import print_function
from influx_poster import database_post
from threading import Thread
from time import sleep, time
import datetime
import csv
import subprocess
import sys
import os
import signal
 
class bluetoothManager_scale(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.exit = 0
 
    def endBluetooth(self): 
        self.exit = 1

    def run(self):
        try:
            count = 0
            process = subprocess.Popen("exec /usr/bin/gatttool -b EB:3D:C2:2D:A5:F4 -t random --char-write-req -a 0x0025 -n 0100 --listen", shell=True, stdout=subprocess.PIPE)
            count2 = 0
            output = ""
            for line in iter(process.stdout.readline, ''):
                if (count < 2): 
                    count = count + 1
                else:
                    output = line[36:].replace(" ", "").strip()
                    output = output.decode('hex')
                    output = output.replace(",kg,", "")
                    value = output.rstrip()
                    tag = "scale"
                    dbpost = database_post(tag, value)
                    dbpost.start()
                    timestamp = datetime.datetime.now()
                    timestring = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    with open("/home/jzc/logs/scale.csv", "a") as csvfile: 
                        showerwriter = csv.writer(csvfile, delimiter=',')
                        showerwriter.writerow([timestring, tag, value])
                            
                if(self.exit) :
                    print("attempting exit")
                    process.kill()
                    raise Exception("bluetooth ended")
        except Exception as error :
            print(repr(error))

    