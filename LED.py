#!/usr/bin/env python2.7

import bibliopixel
from bibliopixel.drivers import serial_driver
from bibliopixel.led import *

import ticker

# Causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

#Load driver for the AllPixel

#set number of pixels & LED type here
driver = serial_driver.DriverSerial(num=80, type=serial_driver.LEDTYPE.LPD8806)

#load the LEDStrip class
led = LEDStrip(driver)

#load channel test animation
anim = ticker.Ticker(led)

try:
    #run the animation
    anim.run()
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()
