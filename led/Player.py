from __future__ import print_function

import copy, json, random
from . import FlipFlop, Handler, Looper, Presets, Scroller

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

class Player(bibliopixel.animation.BaseStripAnim):
    DONT_RECORD = 'lL0123456789)!@#$%^&*('

    def __init__(self, internal_delay=4, number=80):
        driver = DriverSerial(num=number, type=LEDTYPE.LPD8806)
        self.led = bibliopixel.led.LEDStrip(driver)
        super(Player, self).__init__(self.led)
        self.led._internalDelay = internal_delay
        self.scroller = Scroller.Scroller()
        self.blacked_out = FlipFlop.FlipFlop('blackout')
        self.looper = Looper.Looper()
        self.handler = Handler.handler(self)
        self.presets = Presets.Presets()

    def step(self, amt=1):
        self._step += 1
        self.looper.step(self.keyboard)
        self.scroller.step(self.led)

    def keyboard(self, c):
        command = self.handler.get(c)
        if command:
            command()
            if c not in self.DONT_RECORD:
                self.looper.event(c)
        else:
            print('Don\'t understand character', c, ord(c))

    def clear_blackout(self):
        self.blacked_out and self.blackout()

    def randomize(self, randomizer=lambda: random.randint(0, 255)):
        self.clear_blackout()
        print('randomizing')
        for i in xrange(len(self.led.buffer)):
            self.led.buffer[i] = int(max(0, min(255, randomizer())))

    def blackout(self):
        if not self.blacked_out:
            self.saved = self.led.buffer
            self.clear()
        else:
            self.led.buffer = self.saved
        self.blacked_out.change()

    def preset(self, i):
        self.clear_blackout()
        preset = self.presets.preset(i)
        if preset:
            scroller, self.led.buffer, looper = preset
            self.scroller = Scroller.Scroller(**scroller)
            self.looper = Looper.Looper(**looper)

    def serialize(self):
        return (self.scroller.serialize(),
                copy.deepcopy(self.led.buffer),
                self.looper.serialize())

    def set_preset(self, i):
        self.clear_blackout()
        self.presets.set_preset(i, self.serialize())

    def clear(self):
        self.clear_blackout()
        self.led.buffer = len(self.led.buffer) * [0]

    def exit(self):
        self.led.all_off()
        self.led.update()
