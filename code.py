from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware  # for Pico RGB Keypad Base

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keypad
keypad = PMK(Hardware())
keys = keypad.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


# The regular map of keycodes that will be mapped sequentially to each of the keys, 0-15
# If calling multiple keystrockes, put each sequence as a list in a list
n_keymap =    [
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

             [Keycode.B],             # Button 6

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]],          # Button 2

             [Keycode.C],             # Button F

             [Keycode.D],             # Button B

             [Keycode.E],             # Button 7

             [[Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.L],
             [Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.U]]           # Button 3
             ]


# The shifted map of keycodes that will be mapped sequentially to each of the keys, 0-15
# If calling multiple keystrockes, put each sequence as a list in a list
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

# The colours to be set by pressing the keys
l_blue = (0, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

step_buttons = [3, 7, 11, 15]
jog_buttons = [1, 4, 5, 9, 12, 13]

jog_enable = False
shift_enable = True

# Attach handler functions to all of the keys
for key in keys:

    # A press handler that sends the keycode and turns on the LED

    @keypad.on_press(key)
    def press_handler(key):
        global jog_enable
        global timestamp

        print("Keynumber:", key.number)

        if key.number in step_buttons:

            for button in keys[3::4]:
                button.led_off()

            jog_enable = True
            key.set_led(*yellow)
            print(jog_enable)
            print(keypad.time_of_last_press)

            for entry in keymap[key.number]:    # Used to send multiple Keystrokes
                keyboard.send(*entry)
                print("Keynumber:", key.number)
                print("Typ:", type(keymap[key.number]))

#            timestamp = keypad.time_of_last_press


        elif key.number in jog_buttons and jog_enable == False:
            key.set_led(*red)
            print("Jog enable:", jog_enable)
            print("Lastpress:", keypad.time_of_last_press)
            print("Timestamp:", timestamp)

        else:
            keyvalue = keymap[key.number]
            keyboard.send(*keyvalue)
            key.set_led(*l_blue)
#            timestamp = keypad.time_of_last_press
#            print("Typ:", type(keymap[key.number]))
            print("Jog enable:", jog_enable)
            print("Lastpress:", keypad.time_of_last_press)
            print("Timestamp:", timestamp)

    # A release handler that turns off the LED
    @keypad.on_release(key)
    def release_handler(key):

        print(timestamp)

        if key.number not in step_buttons:
            key.led_off()

keymap = []

while True:

    keypad.update()

    keypad.led_sleep_enabled = True
    keypad.led_sleep_time = 5

# Sleeping all led and disbling the jogging buttons
    if keypad.sleeping:
        jog_enable = False

# Switching from normal keymap to shifted keymap
    if keys[0].held:
        keymap = s_keymap
    else:
        keymap = n_keymap

    """
    if keypad.time_of_last_press > (timestamp + 5):
        jog_enable = False
    """

