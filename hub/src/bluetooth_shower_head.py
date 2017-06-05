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

class bluetoothManager_head(Thread):
 
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.exit = 0
 
    def endBluetooth(self): 
        print("ending shower head")
        self.exit = 1

    def run(self):
        try:
            print("started shower head")
            count = 0
            process = subprocess.Popen("exec /usr/bin/gatttool -b C8:32:82:D2:3E:6A -t random --char-write-req -a 0x23 -n 0100 --listen", shell=True, stdout=subprocess.PIPE)
            buffer = ""           
            for line in iter(process.stdout.readline, ''):
                
                if(self.exit) :
                    print("attempting exit")
                    process.kill()
                    raise Exception("bluetooth ended")

                if (count < 10) : 
                    count = count + 1
                else :                     
                    try: 
                        input = line[36:].replace(" ", "").strip()
                        buffer += input.decode('hex')
                        if(buffer.find('*') > -1) :
                            output = buffer[:buffer.find('*')]
                            selector = output[0]
                            array = output[1:].split(',')
                            if(len(array) == 3) :
                                if(selector == 'a' or selector == 'm' or selector == 'g') :
                                    database_post(selector + "x", array[0], "head").start()
                                    database_post(selector + "y", array[1], "head").start()
                                    database_post(selector + "z", array[2], "head").start()
                                    timestamp = datetime.datetime.now()
                                    timestring = timestamp.strftime("%Y-%m-%d %H:%M:%S:%f")
                                    with open("/home/jzc/logs/head.csv", "a") as csvfile: 
                                        showerwriter = csv.writer(csvfile, delimiter=',')
                                        showerwriter.writerow([timestring, selector + "x", array[0]])
                                        showerwriter.writerow([timestring, selector + "y", array[1]])
                                        showerwriter.writerow([timestring, selector + "z", array[2]])
                            buffer = buffer[buffer.find('*')+1:]
                    except ValueError as verror :
                        print("my special verror")
                        print(repr(verror))
                        buffer = "" 
                        continue 
                    except IndexError as ierror :
                        print("my special ierror")
                        print(repr(ierror))
                        buffer = "" 
                        continue

                
        except Exception as error :
            process.kill()
            print(repr(error))

    