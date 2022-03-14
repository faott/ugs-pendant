# ugs-pendant
Universal G-Code Sender CNC Pendant

## Important
The Code is still in development. 

## Based on the following Hard- and Software
### Hardware
Pimoroni 4x4 RGB Button Board for Raspberry Pi Pico
The related Software is available on github:  
[Pimoroni / PMK Circuitpython](https://github.com/pimoroni/pmk-circuitpython)

### Software
The Code is written with CircuitPython and the according Adafruit Libraries for creating an  HID Device
An example related to the Hardware is available on github: 
[Pimoroni / HID Key Sample](https://github.com/pimoroni/pmk-circuitpython/blob/main/examples/hid-keys-simple.py)
The Documentation for the HID Library can be found here: 
[Circuitpython HID Documentation](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode)

## Funcionality
### Jog Step Selection
The Buttons Labled on the Board with **0/1/2/3** will be used to select the desired step size for both, the x and y, as well as the z axis. Before you can change jog any of the axis you first have to select a stepsize. This due to the lack of synchronizing between the PC and the Keypad, so you don't accidentally jog with a different step size then selected on the keypad.

- If none of the step selection buttons is enabled, the jog buttons will light up red.
- If the step selection is enebled, the buttons light up blue.

### Jog Buttons
The jog buttons will move the labled axis according to the selected stepsize.

### Shift Button
The shift button **C** will enable the shifted keymap. This does not only provides additional keys to be used but also implements some securty for certain functions like the Send G-Code command.

- Sending the G-Code command to the machine, witch means that the spindel will start and the carving will start can only be done if the shift button is pressed.

### Play, Pause, Stop Buttons
The carving can be controlled with these buttons. The play (send G-Code) button can only be pressed with the shift button enabled, otherwise it will call the Keystroke for pause.

