from __future__ import print_function

import random
import scroller

from bibliopixel import animation, colors

class Ticker(animation.BaseStripAnim):
    def __init__(self, led):
        super(Ticker, self).__init__(led)
        self._internalDelay = 4
        self.scroller = scroller.Scroller(self._internalDelay)

    def scroll(self, steps):
        self.scroller.scroll(self._led, steps)

    def step(self, amt=1):
        if not self._step:
            self.randomize()

        self._step += 1
        self.scroller.step(self._led)

    def randomize(self, randomizer=lambda: random.randint(0, 255)):
        print('randomizing')
        for i in xrange(len(self._led.buffer)):
            self._led.buffer[i] = int(max(0, min(255, randomizer())))
