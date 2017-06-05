from bluetooth_shower_head import bluetoothManager_head
from bluetooth_scale import bluetoothManager_scale
from influx_poster import database_post

import signal
import sys
import time

if __name__ == '__main__':
   runtime = 480
   try:
      database_post("indicator", 1.0, "startstop").start()
      print("instatiating threads")
      shower_head_thread = bluetoothManager_head()
      shower_scale_thread = bluetoothManager_scale()
      print("starting head thread")
      shower_head_thread.start()
      time.sleep(5)
      print("starting scale thread")
      shower_scale_thread.start()
      print("running for " + str(runtime) + " please waite")
      time.sleep(runtime)
      print("ending thread")
      database_post("indicator", 0.0, "startstop").start()
      shower_head_thread.endBluetooth()
      shower_scale_thread.endBluetooth()

   except KeyboardInterrupt:
      print("W: interrupt received, stopping")
      shower_head_thread.endBluetooth()
      shower_scale_thread.endBluetooth()

   except Exception as error:
      shower_head_thread.endBluetooth()
      shower_scale_thread.endBluetooth()
      print(repr(error))

   finally:
      print("cleaning up")

 



