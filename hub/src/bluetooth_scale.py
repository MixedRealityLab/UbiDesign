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
                    output = output + line[36:].replace(" ", "").strip()
                    print(output)       
                if(self.exit) :
                    print("attempting exit")
                    process.kill()
                    raise Exception("bluetooth ended")
        except Exception as error :
            print(repr(error))

    