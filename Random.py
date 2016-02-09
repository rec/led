#!/usr/bin/env python2.7

from __future__ import print_function

import random

def basic(i=None):
    return random.randint(0, 255)

def filterer(rand, ratio):
    def func(i=None):
        return rand() if random.random() < ratio else 0
    return func

def expo(i=None):
    return random.expovariate(1 / 127.0)
