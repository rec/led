from bibliopixel import animation, colors

class Ticker(animation.BaseStripAnim):
    def __init__(self, led):
        super(Ticker, self).__init__(led)
        self._internalDelay = 4
        self.running = True
        self.last_scroll = 0
        self.period_in_steps = 125
        self.direction = 1

    def scroll(self, steps):
        led = self._led
        steps = steps % led.numLEDs
        # https://stackoverflow.com/questions/9457832/python-list-rotation
        led.buffer = led.buffer[-3 * steps:] + led.buffer[:-3 * steps]

    def step(self, amt = 1):
        if not self._step:
            self.setme()

        self._step += 1
        if self.period_in_steps:
            if self.last_scroll >= self.period_in_steps:
                self.last_scroll = 0
                self.scroll(self.direction)
            else:
                self.last_scroll += 1

    def change_speed(self, increment):
        if self.direction < 0:
            increment = -increment
        if not self.period_in_steps:
            self.direction = abs(increment) / increment
            self.period_in_steps = 1
        else:
            self.period_in_steps *= 1.0 + increment / 100.0
            if self.period_in_steps < 1:
                self.period_in_steps = 0
        print 'speed is now', self.period_in_steps

    def change_color(self, color_index, increment):
        self._led.buffer[color_index] = (
            (self._led.buffer[color_index] + increment) % 256)

    def setme(self):
        self._led.set(0, colors.Red)
        self._led.set(1, colors.Green)
        self._led.set(2, colors.Green)
        self._led.set(3, colors.Blue)
        self._led.set(4, colors.Blue)
        self._led.set(5, colors.Blue)
