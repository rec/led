from __future__ import print_function

import copy, json, random, serial
from . import Animation, FlipFlop, Handler, Looper, Presets, Scroller

class Player(object):
    DONT_RECORD = 'lL0123456789)!@#$%^&*('

    def __init__(self, **kwds):
        self.animation = Animation.animation(**kwds)
        self.animation.step = self.step

        self.blacked_out = FlipFlop.FlipFlop('blackout')

        self.scroller = Scroller.Scroller()
        self.looper = Looper.Looper()
        self.handler = Handler.handler()
        self.presets = Presets.Presets()

    def buffer(self):
        return self.animation._led.buffer

    def step(self, amt=1):
        self.animation._step += 1
        self.looper.step(self.keyboard)
        self.scroller.step(self.buffer())

    def keyboard(self, c):
        command = self.handler.get(c)
        if command:
            command(self)
            if c not in self.DONT_RECORD:
                self.looper.event(c)
        else:
            print('Don\'t understand character', c, ord(c))

    def clear_blackout(self):
        self.blacked_out and self.blackout()

    def blackout(self):
        if not self.blacked_out:
            self.saved = self.buffer()
            self.clear()
        else:
            self.buffer()[:] = self.saved
        self.blacked_out.change()

    def preset(self, i):
        self.clear_blackout()
        preset = self.presets.preset(i)
        if preset:
            self.buffer()[:] = preset['buffer']
            self.scroller = Scroller.Scroller(**preset['scroller'])
            self.looper = Looper.Looper(**preset['looper'])

    def serialize(self):
        return {'scroller': self.scroller,
                'buffer': self.buffer,
                'looper': self.looper}

    def set_preset(self, i):
        self.clear_blackout()
        self.presets.set_preset(i, self)

    def clear(self):
        self.clear_blackout()
        self.animation._led.buffer = len(self.animation._led.buffer) * [0]

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
        self.animation._led.all_off()
        self.animation._led.update()
