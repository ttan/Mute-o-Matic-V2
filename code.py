import board
import time
import usb_hid

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

switch = DigitalInOut(board.GP4)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

bt1 = DigitalInOut(board.GP18)
bt1.direction = Direction.INPUT
bt1.pull = Pull.UP

bt2 = DigitalInOut(board.GP20)
bt2.direction = Direction.INPUT
bt2.pull = Pull.UP

led = DigitalInOut(board.GP10)
led.direction = Direction.OUTPUT

keyboard=Keyboard(usb_hid.devices)

bt1Released = True
bt2Released = True

while True:
    if not bt1.value and bt1Released:
        bt1Released = False
        if switch.value:
            #MacOs
            print("Button 1, Switch position 1")
            led.value = not led.value
            keyboard.send(Keycode.GUI, Keycode.SHIFT, Keycode.M)
        else:
            #Windows
            print("Button 1, Switch position 2")
            led.value = not led.value
            keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
    if not bt2.value and bt2Released:
        bt2Released = False
        if switch.value:
            #MacOs
            print("Button 2, Switch position 1")
            keyboard.send(Keycode.GUI, Keycode.SHIFT, Keycode.B)
        else:
            #Windows
            print("Button 2, Switch position 2")
            keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.B)
    if bt1.value and not bt1Released:
        bt1Released = true
    if bt2.value and not bt2Released:
        bt2Released = true
