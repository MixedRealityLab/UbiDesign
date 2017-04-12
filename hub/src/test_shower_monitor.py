
from wireless_things import SerialManager
import signal
import sys
import time
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
            print("shower running")
         else :
            print("shower not running")

   except KeyboardInterrupt:
      print("W: interrupt received, stopping")
      serialThread.endSerial()

   except Exception as error:
      serialThread.endSerial()

      print(repr(error))

   finally:
      print("cleaning up")

 


