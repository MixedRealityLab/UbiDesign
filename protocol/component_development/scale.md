# Scale
## Components

- 4 * 500g 4 wire wheastone bridge load cells
- 16 * laser cut spacers
- M3 nuts and bolts for attaching load cells // Hysun to confirm lengths
- 2 * laser cut perspex top plate // Laser cutter file #1
- 1 * 3D printed box lid // STL and inventor file #2
- 1 * 3D printed box base // STL and inventor file #3
- 1 * battery compartment lid
- 1 * protoboard strip 2 * 4 holes
- M3 nutes and bolts for mounting PCBs in box
- 3mm 3:1 heat shrink
- 6mm 3:1 heat shrink
- 22 awg single core wire (4 colours inc black and white)
- 4 core white sheathed wire (Yellow, blue, red and black), each core is made up of copper strands for twisting
- Open scale board
- Adafruit BLE UART friend board
- 1 * JST 2 wire assembly
- 1 * 7800 mah 18650 lipo battery
- adafruit powerboot 1000c 
- 3d printed battery compartment lid // STL and inventor file # 4
- 3d printed calibration base // STL and inventor file # 5

## Procedure

### Extend the wire on the load cells by 20cm using cores of the white sheathed wire

- Remove the white sheath of the extension wire using knife to expose 4 coloured wire
- trip and tin both ends of each piece of extension wire (you should have 4 of each colour)
- Strip and tin each wire of the load cells, be careful as these are delicate
- Join the load cell wires to the extension wire using NASA method
- Shrink wrap the joints using 3mm 3:1 shrink wrap

### Wire the load cells in parallel

- These joints have to be made after the wires have been passed throught the perspex base of the shelf and the printed box lid
- You need to join the colours together, i.e. all red wires should be joined, all black wires should be joind
- Join each 4 sets of wires into 1 (the joined wires will be the tinned copper wires). 
- Join each joint of 4 to a different colour of 22awg single core wire, bearing in mind the origin colour (the colour of the wire from the load cell) 
- heat shrink all of these ratger bulky joints using 6mm 3:1 heat shrink

### Attach battery, UART and Voltage Regulator
- join a JST wire assembly to the battery
- Using 22awg wire join the 5v and GND pins of the adafruit micro boost to the 5v gnd terminals of the open scale
- Using 22awg wire join: 
- - TX of serial out on open scale to RXI of BLE UART Friend
- - 5V of serial out on open scale to VIN of BLE UART Friend
- - GND of serial out on open scale to GND of BLE UART Friend

### Conect load cells to open scale (use source wire colour to determine screw terminal to use

### Calibrate open scale
- Without battery connected place scale onto calibration base 
- Connect open scale to PC using USB mini cable
- Using serial terminal connect to open scale at 9600 baud
- press x to bring up menu screen
- remove external and internal temperature readings
- reduce decimal places to 0
- change units to KG
- tare scale
- calibrate scale using known weight
- remove usb cable

### Place items into case
- Fix mounting screws to holes in shower case
- Put PCBs into place and attach to mounting screws
- Route battery lead into battery compartment

### Place scales into shelf





