#!/usr/bin/env python2.7

from __future__ import print_function

import threading
from led import Player, Keyboard

def run():
    player = Player.Player()
    t1 = threading.Thread(target=Keyboard.keyboard, args=(player.keyboard,))
    t2 = threading.Thread(target=player.run_and_exit)
    t1.start()
    t2.start()

run()
