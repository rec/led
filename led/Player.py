from __future__ import print_function

import copy, json, random, serial
from . import FlipFlop, Handler, Looper, Presets, Scroller

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

class Player(object):
    DONT_RECORD = 'lL0123456789)!@#$%^&*('

    def __init__(self, internal_delay=4, number=80):
        driver = DriverSerial(num=number, type=LEDTYPE.LPD8806)
        self.led = bibliopixel.led.LEDStrip(driver)
        self.animation = bibliopixel.animation.BaseStripAnim(self.led)
        self.animation.step = self.step

        self.led._internalDelay = internal_delay
        self.scroller = Scroller.Scroller()
        self.blacked_out = FlipFlop.FlipFlop('blackout')
        self.looper = Looper.Looper()
        self.handler = Handler.handler(self)
        self.presets = Presets.Presets()

    def step(self, amt=1):
        self.animation._step += 1
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
            self.led.buffer = preset['buffer']
            self.scroller = Scroller.Scroller(**preset['scroller'])
            self.looper = Looper.Looper(**preset['looper'])

    def serialize(self):
        return {'scroller': self.scroller,
                'buffer': self.led.buffer,
                'looper': self.looper}

    def set_preset(self, i):
        self.clear_blackout()
        self.presets.set_preset(i, self)

    def clear(self):
        self.clear_blackout()
        self.led.buffer = len(self.led.buffer) * [0]

    def run_and_exit(self):
        try:
            self.animation.run()
        except KeyboardInterrupt:
            pass
        except serial.SerialException:
            pass
        self.exit()

    def exit(self):
        self.animation.stopThread()
        self.led.all_off()
        self.led.update()
