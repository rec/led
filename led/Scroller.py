from __future__ import print_function

import random, time
from . import Serialize

from bibliopixel import animation, colors

class Scroller(object):
    """Represents the state of a scrolling strip of LEDs."""
    def __init__(self, paused=False, frequency=2.0, accumulator=0.0, delta=1):
        self.paused = paused
        self.frequency = frequency
        self.accumulator = accumulator
        self.delta = delta
        self.last_time = time.time()

    def scroll(self, colors, steps):
        colors.rotate(steps)

    def pause(self):
        self.paused = not self.paused
        print('paused.' if self.paused else 'running.')
        if not self.paused:
            self.last_time = time.time()

    def step(self, led):
        if not self.paused:
            t = time.time()
            self.accumulator += (t - self.last_time) * self.frequency
            self.last_time = t

            if self.accumulator >= 1.0:
                steps = int(self.accumulator)
                self.scroll(led, steps)
                self.accumulator -= steps

    def reverse(self):
        self.delta = -self.delta
        print('forward' if self.delta > 0 else 'reverse')

    def change_speed(self, increment):
        ratio = 1.0 + increment / 100.0
        self.frequency /= ratio
        print('Speed is now {:03.3f}Hz'.format(self.frequency))
