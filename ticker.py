from bibliopixel import animation, colors

class Ticker(animation.BaseStripAnim):
    def __init__(self, led):
        super(Ticker, self).__init__(led)
        self._internalDelay = 500
        self.colors =  [colors.Red, colors.Green, colors.Blue, colors.White]

    def step(self, amt = 1):

        self._led.set(0, colors.Red)
        self._led.set(1, colors.Green)
        self._led.set(2, colors.Green)
        self._led.set(3, colors.Blue)
        self._led.set(4, colors.Blue)
        self._led.set(5, colors.Blue)

        color =  self._step % 4
        self._led.fill(self.colors[color], 7, 9)

        self._step += 1
        if self._internalDelay < 100:
            print('here!')
            self._internalDelay = 100
        elif self._internalDelay > 100:
            self._internalDelay -= 11
