from __future__ import print_function

from bibliopixel import animation, colors

class Ticker(animation.BaseStripAnim):
    def __init__(self, led):
        super(Ticker, self).__init__(led)
        self._internalDelay = 4
        self.running = True
        self.last_scroll = 0
        self.period_in_steps = 125
        self.direction = 1
        self.selected = 0
        self.flash_selected = False
        self.flash_toggle_requested = False
        self.flash_period = 20
        self.selected_color = colors.Black

    def scroll(self, steps):
        led = self._led
        steps = steps % led.numLEDs
        # https://stackoverflow.com/questions/9457832/python-list-rotation
        led.buffer = led.buffer[-3 * steps:] + led.buffer[:-3 * steps]

    def toggle_flash_selected(self):
        # For safety, defer toggling the flash until the "main update thread".
        self.flash_toggle_requested = True

    def toggle_pause(self):
        self.running = not self.running
        print('Running.' if self.running else 'Paused.')

    def increment_selected(self, increment=1):
        self.selected = (self.selected + increment) % self._led.numLEDs
        print('Selected is now', self.selected)

    def step(self, amt = 1):
        if not self._step:
            self.setme()

        if self.flash_selected:
            self._led.set(self.selected, self.selected_color)

        if self.flash_toggle_requested:
            self.flash_toggle_requested = False
            self.flash_selected = not self.flash_selected
            print('Flashing.' if self.flash_selected else 'Not flashing.')

        self._step += 1
        if not self.running:
            return
        if self.period_in_steps:
            if self.last_scroll >= self.period_in_steps:
                self.last_scroll = 0
                self.scroll(self.direction)
            else:
                self.last_scroll += 1

    def reverse(self):
        self.direction = -self.direction

    def change_speed(self, increment):
        self.period_in_steps *= 1.0 + increment / 100.0
        if self.period_in_steps < 1:
            self.period_in_steps = 1

        print('speed is now',
              (1000 / self._internalDelay) / self.period_in_steps,
              'LEDs per second')

    def change_color(self, color_index, increment):
        i = color_index + 3 * self.selected
        self._led.buffer[i] = (self._led.buffer[i] + increment) % 256

    def setme(self):
        self._led.set(0, colors.Red)
        self._led.set(1, colors.Green)
        self._led.set(2, colors.Green)
        self._led.set(3, colors.Blue)
        self._led.set(4, colors.Blue)
        self._led.set(5, colors.Blue)
