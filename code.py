from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware  # for Pico RGB Keypad Base

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
keypad = PMK(Hardware())
keys = keypad.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


# A map of keycodes that will be mapped sequentially to each of the keys, 0-15
keymap =    [
             [Keycode.THREE],           # Button C

             [Keycode.ONE, Keycode.T],  # Button 8

             [Keycode.U],               # Button 4

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]],         # Button 0

             [Keycode.FOUR],          # Button D

             [Keycode.FIVE],          # Button 9

             [Keycode.SIX],           # Button 5

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]],          # Button 1

             [Keycode.EIGHT],         # Button E

             [Keycode.NINE],          # Button A

             [Keycode.A],             # Button 6

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]],          # Button 2

             [Keycode.C],             # Button F

             [Keycode.D],             # Button B

             [Keycode.E],             # Button 7

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]]           # Button 3
             ]

s_keymap =  [
             [],            # Button C

             [],            # Button 8

             [],            # Button 4

             [],            # Button 0

             [],            # Button D

             [],            # Button 9

             [],            # Button 5

             [],            # Button 1

             [],            # Button E

             [],            # Button A

             [Keycode.A],   # Button 6

             [],            # Button 2

             [],            # Button F

             [],            # Button B

             [],            # Button 7

             []             # Button 3
             ]

"""
print(keymap2[1])
print(keys)
print(Keycode.LEFT_CONTROL)
"""

# The colour to set the keys when pressed, yellow.
l_blue = (0, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)


shift = False

step_buttons = [3, 7, 11, 15]
jog_buttons = [1, 4, 5, 9, 12, 13]

jog_enable = False

# Attach handler functions to all of the keys
for key in keys:
    # A press handler that sends the keycode and turns on the LED

    @keypad.on_press(key)
    def press_handler(key):
        global jog_enable

        print("Keynumber:", key.number)

        if key.number in step_buttons:
            jog_enable = True
            key.set_led(*yellow)
            print(jog_enable)
            for entry in keymap[key.number]:    # Used to send multiple Keystrokes
                keyboard.send(*entry)
                print("Keynumber:", key.number)
                print("Typ:", type(keymap[key.number]))


        elif key.number in jog_buttons and jog_enable == False:
            key.set_led(*red)
            print(jog_enable)

        else:
            keyvalue = keymap[key.number]
            keyboard.send(*keyvalue)
            key.set_led(*l_blue)
            print("Typ:", type(keymap[key.number]))
            print(jog_enable)

    # A release handler that turns off the LED
    @keypad.on_release(key)
    def release_handler(key):
        key.led_off()


while True:
    # Always remember to call keypad.update()!
    keypad.update()