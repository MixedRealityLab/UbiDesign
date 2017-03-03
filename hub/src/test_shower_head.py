from bluetooth_shower_head import bluetoothManager_head
import signal
import sys
import time

if __name__ == '__main__':
   
   try:
      print("instatiating thread")
      shower_head_thread = bluetoothManager_head()
      print("starting thread")
      shower_head_thread.start()
      print("wait 10 seconds")
      time.sleep(15)
      print("ending thread")
      shower_head_thread.endBluetooth()

   except KeyboardInterrupt:
      print("W: interrupt received, stopping")
      shower_head_thread.endBluetooth()

   except Exception as error:
      shower_head_thread.endBluetooth()
      print(repr(error))

   finally:
      print("cleaning up")

 


