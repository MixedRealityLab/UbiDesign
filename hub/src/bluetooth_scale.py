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
        print("ending scale")
        self.exit = 1

    def run(self):
        try:
            print("started scale")
            count = 0
            tare = 0
            tared = False
            process = subprocess.Popen("exec /usr/bin/gatttool -b EB:3D:C2:2D:A5:F4 -t random --char-write-req -a 0x23 -n 0100 --listen", shell=True, stdout=subprocess.PIPE)
            buffer = ""           
            for line in iter(process.stdout.readline, ''):
                if (count < 3) : 
                    count = count + 1

                else :                     
                    input = line[36:].replace(" ", "").strip()
                    buffer += input.decode('hex')
                    if(buffer.find('\n') > -1) :
                        output = buffer[:buffer.find('\n')]
                        try:
                            output = float(output.replace(",kg,", ""))
                            if(tared == False):
                                print("taring")
                                tare = output
                                print("tared")
                                tared = True
                            else: 
                                value = tare - output
                                tag = "scale"
                                dbpost = database_post(tag, value, "scale")
                                dbpost.start()
                                timestamp = datetime.datetime.now()
                                timestring = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                                with open("/home/jzc/logs/scale.csv", "a") as csvfile: 
                                    showerwriter = csv.writer(csvfile, delimiter=',')
                                    showerwriter.writerow([timestring, tag, value])
                                print(value)
                        except ValueError as error:
                            print(repr(error))

                        
                        buffer = buffer[buffer.find('\n')+1:]                                          
                if(self.exit) :
                    print("attempting exit")
                    process.kill()
                    raise Exception("bluetooth ended")
        except Exception as error :
            process.kill()
            print(repr(error))

    

    
