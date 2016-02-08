#!/usr/bin/env python2.7

import random

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

import scroller

class LED(bibliopixel.animation.BaseStripAnim):
    def __init__(self, internal_delay=4, number=80):
        driver = DriverSerial(num=number, type=LEDTYPE.LPD8806)
        self.led = bibliopixel.led.LEDStrip(driver)
        super(LED, self).__init__(self.led)
        self.led._internalDelay = internal_delay
        self.scroller = scroller.Scroller(self.led)

    def step(self, amt=1):
        if not self._step:
            self.randomize()

        self._step += 1
        self.scroller.step(self.led._internalDelay)

    def scroll(self, steps):
        self.scroller.scroll(steps)

    def randomize(self, randomizer=lambda: random.randint(0, 255)):
        print('randomizing')
        for i in xrange(len(self.led.buffer)):
            self.led.buffer[i] = int(max(0, min(255, randomizer())))

    def exit(self):
        self.led.all_off()
        self.led.update()
