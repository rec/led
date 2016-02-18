#!/usr/bin/env python2.7

from __future__ import print_function

import serial
from led import Player, Keyboard

player = Player.Player()

thread = Keyboard.threaded(player.keyboard)

try:
    player.run()
except KeyboardInterrupt:
    pass
except serial.SerialException:
    pass

player.exit()
