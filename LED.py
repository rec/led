from __future__ import print_function

import json, random, FlipFlop, Handler, Looper, Scroller
from copy import deepcopy

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

PRESET_FILE = '.presets'

class LED(bibliopixel.animation.BaseStripAnim):
    def __init__(self, internal_delay=4, number=80):
        driver = DriverSerial(num=number, type=LEDTYPE.LPD8806)
        self.led = bibliopixel.led.LEDStrip(driver)
        super(LED, self).__init__(self.led)
        self.led._internalDelay = internal_delay
        self.scroller = Scroller.Scroller()
        self.blacked_out = FlipFlop.FlipFlop('blackout')
        self.handler = Handler.handler(self)
        self.looper = Looper.Looper()
        try:
            fp = open(PRESET_FILE)
        except:
            self.presets = 10 * [None]
        else:
            self.presets = json.load(fp)

    def step(self, amt=1):
        self._step += 1
        self.scroller.step(self.led)

    def keyboard(self, c):
        command = self.handler.get(c)
        if command:
            command()
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
        preset = self.presets[i]
        if preset:
            scroller, self.led.buffer, looper = preset
            self.scroller = Scroller.Scroller(**scroller)
            self.looper = Looper.Looper(**looper)
            print('Loaded preset', i)
        else:
            print('No preset stored at', i)

    def set_preset(self, i):
        self.clear_blackout()
        self.presets[i] = (
            self.scroller.serialize(),
            deepcopy(self.led.buffer),
            self.looper.serialize())
        json.dump(self.presets, open(PRESET_FILE, 'w'))
        print('Stored preset at', i)

    def clear(self):
        self.clear_blackout()
        self.led.buffer = len(self.led.buffer) * [0]

    def exit(self):
        self.led.all_off()
        self.led.update()
