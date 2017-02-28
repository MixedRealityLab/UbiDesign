# Shower Monitor
## Components

- 200 * 120 * 75mm  IP65 enclosure
- M25 nylon cable gland and lock nut
- 150mm * 15mm copper pipe
- 1 wire water flow sensor
- 2 * Shower hose washer (0.5")
- 0.5" BSP Shower hose
- 150mm * 15mm push fit to 0.5" BSP hose
- 15mm push fit to 0.5" BSP plastic adapter
- 1 Wire temperature sensor
- 2 * 10K through hole resistor
- 3.3v TC1015 regulator
- 1 * 4pin 2.54mm header
- rfµ328 wireless things board
- 75mm antenna wire
- rfµ328 dec board
- 2 * 10 pin 2mm headers
- 2 * 10 pin 2mm sockets
- 1 * JST 2 wire female PCB connector
- 1 * JST 2 wire assembly
- 1 * 7800 mah 18650 lipo battery
- 22awg single core hookup wire
- insulation tape
- thermal paste

## Procedure

### Prepare enclosure
- Cut copper pipe to length
- Drill 25mm hole in centre of both ends of enclosure (allowing assembly to pass through lenthways
- Fit M25 gland to to hole of enclosre
- place copper pipe though gland and secure using adjustable spanner, leaving enough exposed outside of box to attach pushfit to 0.5" BSP hose

### Assemble electronics
- solder 2mm headers to RFµ328 Board
- Solder antenna to RFµ328 board using top centre hole next to 328 text printing
- Solder 2mm sockets to 328 dev board
- Solder JST socket to 328 dev board
- Solder 2.54mm header to TC1015 regulator
- Solder regulator assembly to position marked on dev board
- The flow sensor needs to be soldered; black to ground, red to 3.3v, yellow to both pin 11 (top right pin) of RFµ 328 and to 3.3v via 10k resistor 
- The temperature sensor needs to be soldered; black to ground, red to 3.3v, yellow to both pin 12 (1 below top right pin) of RFµ 328 and to 3.3v via 10k resistor 
- Solder JST wire assmbly to battery
- program RFµ328 using wireless things voyager in serial socket mode and arduno IDE, flash firmware file shower_mointor.ino

### Attach electronics to enclosure 
- Place thermal paste on body of temperature sensor probe end and attach to copper pipe using insulation tape
- Attach flow sensor input end to copper pipe using 15mm push fit to 0.5" BSP plastic adapter, put PTFE tape on threads
- Thread shower hose through bottom hole of enclosure and attach to output of flow sensor making sure 0.5" washer is inside connection
- Fully charge battery using lipo charger and attach to electronics board
- Place lid on enclosure. 

## Testing

To test you should connect assembled unit to shower oulet via 50mm * 15mm push fit to 0.5" BSP hose and run the shower. If you put the wireless thigns voyager into SRF mode (switch on board for this) then you should be able to connect to this over USB serial at 9600 baud and see the readings from the shower.

Alternatively you can ssh into the hub and run
``` 
sudo python test_shower_monitor.py 

```
then connect to the hub using a web browser on port 8083, select the shower database and query for recent readings

## Comissioning

- The battery should be fully charged and will last a minimum of 15 days from full
- Place battery in box and connect to the electronics board
- Place lid onto box and screw down
- The device should be connected to the participants shower and testing should be completed to ensure correct functionality
- Be aware of the metal BSP conector attaching to plastic shower outlets and avoid overtightening. Use PTFE tape rather than overtightening to avoid leaks.



