from __future__ import print_function

import random

from bibliopixel import animation, colors

class Ticker(animation.BaseStripAnim):
    def __init__(self, led):
        super(Ticker, self).__init__(led)
        self._internalDelay = 4
        self.paused = True
        self.last_scroll = 0
        self.period_in_steps = 125
        self.direction = 1

    def scroll(self, steps):
        led = self._led
        steps = steps % led.numLEDs
        # https://stackoverflow.com/questions/9457832/python-list-rotation
        led.buffer = led.buffer[-3 * steps:] + led.buffer[:-3 * steps]

    def pause(self):
        self.paused = not self.paused
        print('paused.' if self.paused else 'running.')

    def step(self, amt=1):
        if not self._step:
            self.randomize()

        self._step += 1
        if not self.paused:
            if self.period_in_steps:
                if self.last_scroll >= self.period_in_steps:
                    self.last_scroll = 0
                    self.scroll(self.direction)
                else:
                    self.last_scroll += 1

    def reverse(self):
        self.direction = -self.direction

    def change_speed(self, increment):
        self.period_in_steps *= 1.0 + increment / 100.0
        if self.period_in_steps < 1:
            self.period_in_steps = 1

        print('speed is now',
              (1000 / self._internalDelay) / self.period_in_steps,
              'LEDs per second')

    def randomize(self, randomizer=lambda: random.randint(0, 255)):
        print('randomizing')
        for i in xrange(len(self._led.buffer)):
            self._led.buffer[i] = int(max(0, min(255, randomizer())))
