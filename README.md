# Mute-o-Matic V2

Hardware mute button and end call for MS Teams, with led indicator. Since I'm using both macOs and Windows, it has a nice and comfortable slide SPST switch on the side to select OS.

This was my test project for the new Raspberry Pi Pico; with ~4€ you get a crazy good microprocessor and implementing HID functionality is extremelty trivial.

The project is written in CircuitPython, using the [Adafruit HID Library](https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html). I used a transparent plastic container because... well, that's the only thing I had in the house and there's lockdown due to COVID-19. Feel free to buy me a 3D Printer ❤️

![Mute-o-matic from the top](https://github.com/ttan/Mute-o-Matic-V2/blob/main/img/IMG_4674.jpg?raw=true)

## A random Fritzing here

This is just to give you a idea of what's doing what.

![Fritzing](https://github.com/ttan/Mute-o-Matic-V2/blob/main/img/mute-o-matic.png?raw=true)

## How it works
🚀 Rocket science! Jokes aside, it's just a HID which sends shortcuts defined in MS Teams, according to the OS selected with the side switch.
For Windows:
- *CTRL + Shift + M* to toggle the mute (and the led)
- *CTRL + Shift + B* to close the call (for strange reasons, this is not a documented shortcut on Teams official page)

For macOs (For macOs, cmd is mapped to GUI. I guess in Windows this would be the Windows logo):
- *CMD + Shift + M* to toggle the mute (and the led)
- *CMD + Shift + B* to close the call (guess what, this is also not a documented shortcut on Teams official page)

Easy. I just needed something to quickly mute/unmute the calls because I tend to get distracted and racing to find the proper button with the mouse is too hard.

## Parts used
- (Raspberry Pi Pico)[https://www.raspberrypi.org/documentation/pico/getting-started/]
- 2 x Panel mount push button (Normally open)
- 1 x Red Led
- 1 x SPST slide switch
- 1 X 220 ohm resistance

## Windows only improvement
On my personal version of the Mute-o-Matic V2, I included another command which brings Teams on focus before toggling mute. This can be done with an idiot trick: pin Teams' icon in the bar (how is it called? the one below) and count what number is it starting from the left. You can switch to that with the shortcut: 
```
Alt + [Number]
```
You will need to do this twice because Teams will have two windows, the first one with the chat and all the other stuff and the second one with your active call. So, let's say I've put the icon as third in my Windows bar, the correct sequence will be:
```
Alt + 3
Alt + 3
CONTROL + Shift + M
```
