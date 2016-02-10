from __future__ import print_function

import time, Saveable

class Looper(Saveable.Saveable):
    """Represents the state of a loop of events."""
    _IGNORE = ('loop_start', 'loop_index', )

    RECORD, PAUSE, PLAY = xrange(3)

    def __init__(self, state=PAUSE, events=None, loop_length=0):
        self.state = state or Looper.PAUSE
        self.events = events or []
        self.loop_length = loop_length
        self.loop_start = 0
        self.loop_index = 0

    def event(self, key):
        if self.state == Looper.RECORD:
            self.events.append((time.time() - self.loop_start, key))

    def clear(self):
        self.state = Looper.PAUSE
        self.events = []

    def set_state(self, state):
        if state != self.state:
            t = time.time()
            if self.state == Looper.RECORD:
                self.loop_length = t - self.loop_start
                self.loop_start = 0
                self.loop_index = 0
            elif self.state == Looper.PLAY:
                self.loop_start = t - self.loop_start
            self.state = state
            if self.state == Looper.PLAY:
                self.loop_start = t - self.loop_start
            if self.state == Looper.RECORD:
                self.events = []
            self.loop_start = t

    def record(self):
        """Toggle record."""
        self.set_state(Looper.PLAY if self.state == Looper.RECORD
                       else Looper.RECORD)

    def play(self):
        self.set_state(Looper.PLAY if self.state == Looper.PAUSE
                       else Looper.PLAY)

    def step(self, callback):
        def emit(dt):
            while self.loop_index < len(self.loop):
                etime, key = self.events[self.loop_index]
                if etime > dt:
                    break
                callback(key)
                self.loop_index += 1

        if self.state == Looper.PLAY:
            t = time.time()
            dt = t - self.loop_start
            emit(min(dt, self.loop_length))
            if dt >= self.loop_length:
                self.loop_index = 0
                dt -= self.loop_length
                self.loop_start = t - dt
                emit(dt)
