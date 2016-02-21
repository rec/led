#!/usr/bin/env python2.7

from __future__ import print_function

from . Processor import basic, expo, filterer, randomize

class Handler(object):
    def __init__(self, desc, function, *args, **kwds):
        self.desc = desc
        self.function = function
        self.args = args
        self.kwds = kwds

    def __call__(self):
        return self.function(*args, **kwds)

def handler():
    table = {
        'q': lambda led: led.animation.exit(),
        '+': lambda led: led.scroller.change_speed(-10),
        '=': lambda led: led.scroller.change_speed(-10),
        '-': lambda led: led.scroller.change_speed(10),
        '_': lambda led: led.scroller.change_speed(10),
        ' ': lambda led: led.scroller.pause(),
        '/': lambda led: led.scroller.reverse(),
        'b': lambda led: led.blackout(),
        'c': lambda led: led.clear(),
        'l': lambda led: led.looper.play(),
        'L': lambda led: led.looper.record(),
        'r': lambda led: randomize(led, basic),
        's': lambda led: randomize(led, expo),
        't': lambda led: randomize(led, filterer(expo, 0.50)),
        'u': lambda led: randomize(led, filterer(basic, 0.50)),
        'v': lambda led: randomize(led, filterer(expo, 0.20)),
        'w': lambda led: randomize(led, filterer(basic, 0.20)),
        'x': lambda led: randomize(led, filterer(expo, 0.08)),
        'y': lambda led: randomize(led, filterer(basic, 0.12)),
        }

    def presets(i):
        return lambda led: led.preset(i), lambda led: led.set_preset(i)

    digits = '0123456789'
    shifts = ')!@#$%^&*('
    for i in xrange(10):
        table[digits[i]], table[shifts[i]] = presets(i)

    return table
