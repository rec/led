from __future__ import print_function

from . import Animation, FlipFlop, Handler, Looper, Presets, Scroller

class Player(object):
    DONT_RECORD = 'lL0123456789)!@#$%^&*('

    def __init__(self, **kwds):
        self.animation = Animation.Animation(step=self.step, **kwds)
        self.colors = self.animation.colors
        self.blacked_out = FlipFlop.FlipFlop('blackout')

        self.scroller = Scroller.Scroller()
        self.looper = Looper.Looper()
        self.handler = Handler.handler()
        self.presets = Presets.Presets()

    def step(self, amt=1):
        self.looper.step(self.keyboard)
        self.scroller.step(self.colors)

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
            self.saved = self.colors[:]
            self.clear()
        else:
            self.colors[:] = self.saved
        self.blacked_out.change()

    def preset(self, i):
        self.clear_blackout()
        preset = self.presets.preset(i)
        if preset:
            self.colors[:] = preset['colors']
            self.scroller = Scroller.Scroller(**preset['scroller'])
            self.looper = Looper.Looper(**preset['looper'])

    def serialize(self):
        return {'scroller': self.scroller,
                'colors': self.colors,
                'looper': self.looper}

    def set_preset(self, i):
        self.clear_blackout()
        self.presets.set_preset(i, self)

    def clear(self):
        self.clear_blackout()
        self.colors[:] = [0] * len(self.colors)

    def run_and_exit(self):
        self.animation.run()
        self.animation.exit()
