from __future__ import print_function

import random, time

from bibliopixel import animation, colors

class Scroller(object):
    """Represents the state of a scrolling strip of LEDs."""
    def __init__(self, led, frequency=2.0):
        self.led = led
        self.paused = False
        self.last_scroll = 0
        self.period_in_steps = 125
        self.frequency = frequency
        self.accumulator = 0.0
        self.delta = 1
        self.last_time = time.time()

    def scroll(self, steps):
        buf = self.led.buffer
        steps = (self.delta * steps) % (len(buf) / 3);
        self.led.buffer = buf[-3 * steps:] + buf[:-3 * steps]
        # From https://stackoverflow.com/questions/9457832

    def pause(self):
        self.paused = not self.paused
        print('paused.' if self.paused else 'running.')
        if not self.paused:
            self.last_time = time.time()

    def step(self):
        if not self.paused:
            t = time.time()
            self.accumulator += (t - self.last_time) * self.frequency
            self.last_time = t

            if self.accumulator >= 1.0:
                steps = int(self.accumulator)
                self.scroll(steps)
                self.accumulator -= steps


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
