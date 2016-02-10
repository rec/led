#!/usr/bin/env python2.7

from __future__ import print_function

import keyboard, serial, LED

led = LED.LED()

thread = keyboard.threaded(led.handler)

try:
    led.run()
except KeyboardInterrupt:
    pass
except serial.SerialException:
    pass

led.exit()
