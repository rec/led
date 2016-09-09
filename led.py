#!/usr/bin/env python3

import led, sys, threading

def run(use_curses=False):
    player = led.Player.Player()
    t1 = threading.Thread(target=player.run_and_exit)
    target = None if use_curses else led.Keyboard.keyboard
    t2 = threading.Thread(target=target, args=(player.keyboard,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    run()
