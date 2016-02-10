#!/usr/bin/env python2.7

from __future__ import print_function

from Random import filterer, expo, basic

def handler(led):
    table = {
        'q': led.exit,
        '+': lambda: led.scroller.change_speed(-10),
        '=': lambda: led.scroller.change_speed(-10),
        '-': lambda: led.scroller.change_speed(10),
        '_': lambda: led.scroller.change_speed(10),
        ' ': led.scroller.pause,
        '/': led.scroller.reverse,
        'b': led.blackout,
        'c': led.clear,
        'r': lambda: led.randomize(basic),
        's': lambda: led.randomize(expo),
        't': lambda: led.randomize(filterer(expo, 0.50)),
        'u': lambda: led.randomize(filterer(basic, 0.50)),
        'v': lambda: led.randomize(filterer(expo, 0.20)),
        'w': lambda: led.randomize(filterer(basic, 0.20)),
        'x': lambda: led.randomize(filterer(expo, 0.08)),
        'y': lambda: led.randomize(filterer(basic, 0.12)),
        }

    def presets(i):
        return lambda: led.preset(i), lambda: led.set_preset(i)

    digits = '0123456789'
    shifts = ')!@#$%^&*('
    for i in xrange(10):
        table[digits[i]], table[shifts[i]] = presets(i)

    return table
