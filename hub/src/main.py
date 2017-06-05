from bluetooth_shower_head import bluetoothManager_head
from bluetooth_scale import bluetoothManager_scale
from wireless_things import SerialManager
from influx_poster import database_post

import signal
import sys
import time
import csv
import datetime

if __name__ == '__main__':
   
   try:
      serialThread = SerialManager()
      serialThread.setName('Serial Manager')
      serialThread.start()
      shower_head_running = 0
      shower_scale_running = 0
      
      while(True) :
         time.sleep(2)
         timediff = datetime.datetime.now() - serialThread.get_last_reading()
         if (timediff.seconds <= 10):
            

            if(shower_head_running == 0):
               database_post("indicator", 1.0, "startstop").start() 
               shower_head_thread = bluetoothManager_head()
               shower_head_thread.start()
               shower_head_running = 1
               time.sleep(5)
            if(shower_scale_running == 0):       
               shower_scale_thread = bluetoothManager_scale()
               shower_scale_thread.start()
               shower_scale_running = 1

         else :
            
            if (shower_head_running) :
               database_post("indicator", 0.0, "startstop").start()
               shower_head_thread.endBluetooth()
               shower_head_running = 0
               time.sleep(5)
            if (shower_scale_running) :
               shower_scale_thread.endBluetooth()
               shower_scale_running = 0

            else :
               pass

   except KeyboardInterrupt:
      print("W: interrupt received, stopping")
      serialThread.endSerial()
      shower_head_thread.endBluetooth()
      shower_scale_thread.endBluetooth()

   except Exception as error:
      serialThread.endSerial()
      shower_head_thread.endBluetooth()
      shower_scale_thread.endBluetooth()
      print(repr(error))

   finally:
      print("cleaning up")

 


