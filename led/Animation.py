from __future__ import print_function

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

def animation(period=4, number=80,
              driver='LPD8806', geometry='Strip', anim=None):
    ds = DriverSerial(num=number, type=getattr(LEDTYPE, driver))
    led = getattr(bibliopixel.led, 'LED' + geometry)(ds)
    led._internalDelay = period
    anim_name = 'Base' + (anim or geometry) + 'Anim'
    return getattr(bibliopixel.animation, anim_name)(led)
