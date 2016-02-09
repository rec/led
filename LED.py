#!/usr/bin/env python2.7

import random

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

import Scroller

class LED(bibliopixel.animation.BaseStripAnim):
    def __init__(self, internal_delay=4, number=80):
        self.number = number
        driver = DriverSerial(num=number, type=LEDTYPE.LPD8806)
        self.led = bibliopixel.led.LEDStrip(driver)
        super(LED, self).__init__(self.led)
        self.led._internalDelay = internal_delay
        self.scroller = Scroller.Scroller(self.led)
        self.blacked_out = False

    def step(self, amt=1):
        if not self._step:
            self.randomize()

        self._step += 1
        self.scroller.step()

    def randomize(self, randomizer=lambda: random.randint(0, 255)):
        self.blacked_out and self.blackout()
        print('randomizing')
        for i in xrange(3 * self.number):
            self.led.buffer[i] = int(max(0, min(255, randomizer())))

    def blackout(self):
        if not self.blacked_out:
            self.saved = self.led.buffer
            self.clear()
        else:
            self.led.buffer = self.saved
        self.blacked_out = not self.blacked_out

    def clear(self):
        self.blacked_out and self.blackout()
        self.led.buffer = 3 * self.number * [0]

    def exit(self):
        self.led.all_off()
        self.led.update()
