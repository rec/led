#!/usr/bin/env python2.7

PATH = '/development/Bibliopixel'
import sys

USE_MASTER = False

if USE_MASTER and PATH not in sys.path:
    sys.path.insert(0, PATH)
# TODO: why does the release version work and git's master crash?


import bibliopixel
from bibliopixel.drivers import serial_driver
from bibliopixel import led

import ticker

class LED(object):
    def __init__(self):
        self.driver = serial_driver.DriverSerial(
            num=80, type=serial_driver.LEDTYPE.LPD8806)
        self.led_strip = led.LEDStrip(self.driver)
        self.ticker = ticker.Ticker(self.led_strip)

    def run(self):
        self.ticker.run()

    def exit(self):
        self.led_strip.all_off()
        self.led_strip.update()


def runner():
    led = LED()

    try:
        led.run()
    except KeyboardInterrupt:
        led.exit()

if __name__ == '__main__':
    runner()
