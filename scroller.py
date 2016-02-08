from __future__ import print_function

import random

from bibliopixel import animation, colors

class Scroller(object):
    """Represents the state of a scrolling strip of LEDs."""
    def __init__(self, led, frequency=0.25):
        self.led = led
        self.paused = False
        self.last_scroll = 0
        self.period_in_steps = 125
        self.frequency = frequency
        self.delta = 1

    def scroll(self, steps):
        buf = self.led.buffer
        steps = steps % (len(buf) / 3);
        self.led.buffer = buf[-3 * steps:] + buf[:-3 * steps]
        # From https://stackoverflow.com/questions/9457832

    def pause(self):
        self.paused = not self.paused
        print('paused.' if self.paused else 'running.')

    def step(self, time_passed):
        if not self.paused:
            if self.period_in_steps:
                if self.last_scroll >= self.period_in_steps:
                    self.last_scroll = 0
                    self.scroll(self.delta)
                else:
                    self.last_scroll += 1

    def reverse(self):
        self.delta = -self.delta

    def change_speed(self, increment):
        ratio = 1.0 + increment / 100.0
        self.period_in_steps *= ratio
        self.frequency /= ratio
        if self.period_in_steps < 1:
            self.period_in_steps = 1

        print('speed is now',
              (1000 / self.led._internalDelay) / self.period_in_steps,
              'LEDs per second or', self.frequency)
