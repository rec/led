#!/usr/bin/env python2.7

from __future__ import print_function

import keyboard, serial, Player

led = Player.Player()

thread = keyboard.threaded(led.keyboard)

try:
    led.run()
except KeyboardInterrupt:
    pass
except serial.SerialException:
    pass

led.exit()
