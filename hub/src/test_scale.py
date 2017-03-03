from bluetooth_scale import bluetoothManager_scale
import signal
import sys
import time

if __name__ == '__main__':
   
   try:
      print("instatiating thread")
      shower_scale_thread = bluetoothManager_scale()
      print("starting thread")
      shower_scale_thread.start()
      print("wait 10 seconds")
      time.sleep(20)
      print("ending thread")
      shower_scale_thread.endBluetooth()

   except KeyboardInterrupt:
      print("W: interrupt received, stopping")
      shower_scale_thread.endBluetooth()

   except Exception as error:
      shower_scale_thread.endBluetooth()
      print(repr(error))

   finally:
      print("cleaning up")