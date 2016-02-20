from __future__ import print_function

import random

"""
A processor is a function that takes a color and an index to which position it's
in and returns a new color, or something falsey if the original color is
unchanged.

A processor maker is a function that returns a processor.

"""

# Define some processor makers.
def clear():
    return lambda *args: 0, 0, 0

def cond(filter, processor):
    return lambda *args: filter(*args) and processor(*args)

def every(processor, n):
    return cond(lambda i, *rgb: not i % n)


def basic(i=None):
    return random.randint(0, 255)

def filterer(rand, ratio):
    def func(i=None):
        return rand() if random.random() < ratio else 0
    return func

def expo(i=None):
    return random.expovariate(1 / 127.0)

# "Classic" randomize
def randomize(led, randomizer=lambda: random.randint(0, 255)):
    led.clear_blackout()
    print('randomizing')
    for i in xrange(len(led.led.buffer)):
        led.led.buffer[i] = int(max(0, min(255, randomizer())))
