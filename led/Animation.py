from __future__ import print_function

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

def animation(step, period=4, number=80,
              driver='LPD8806', geometry='Strip', anim=None):
    ds = DriverSerial(num=number, type=getattr(LEDTYPE, driver))
    led = getattr(bibliopixel.led, 'LED' + geometry)(ds)
    led._internalDelay = period
    anim_name = 'Base' + (anim or geometry) + 'Anim'
    result = getattr(bibliopixel.animation, anim_name)(led)
    def step_function(amt=1):
        result._step += 1
        step()
    result.step = step_function
    return result
