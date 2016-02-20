#!/usr/bin/env python2.7

from __future__ import print_function

import threading
from led import Player, Keyboard

def run(use_curses=False):
    player = Player.Player()
    t1 = threading.Thread(target=player.run_and_exit)
    target = None if use_curses else Keyboard.keyboard
    t2 = threading.Thread(target=target, args=(player.keyboard,))
    t1.start()
    t2.start()

run()
