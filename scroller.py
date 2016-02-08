from __future__ import print_function

import random

from bibliopixel import animation, colors

class Scroller(object):
    """Represents the state of a scrolling strip of LEDs."""
    def __init__(self, frequency=0.5):
        self.paused = True
        self.last_scroll = 0
        self.period_in_steps = 125
        self.frequency = frequency
        self.delta = 1

    def scroll(self, led, steps):
        steps = steps % (len(led.buffer) / 3);
        # https://stackoverflow.com/questions/9457832/python-list-rotation
        led.buffer = led.buffer[-3 * steps:] + led.buffer[:-3 * steps]

    def pause(self):
        self.paused = not self.paused
        print('paused.' if self.paused else 'running.')

    def step(self, led):
        if not self.paused:
            if self.period_in_steps:
                if self.last_scroll >= self.period_in_steps:
                    self.last_scroll = 0
                    self.scroll(led, self.delta)
                else:
                    self.last_scroll += 1

    def reverse(self):
        self.delta = -self.delta

    def change_speed(self, increment):
        self.period_in_steps *= 1.0 + increment / 100.0
        if self.period_in_steps < 1:
            self.period_in_steps = 1

        print('speed is now',
              (1000 / self.internal_delay) / self.period_in_steps,
              'LEDs per second')
