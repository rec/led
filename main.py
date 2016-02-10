#!/usr/bin/env python2.7

from __future__ import print_function

import keyboard, serial, LED, Handler

led = LED.LED()

thread = keyboard.threaded(Handler.handler(led))

try:
    led.run()
except KeyboardInterrupt:
    pass
except serial.SerialException:
    pass

led.exit()
