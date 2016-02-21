from __future__ import print_function

import serial

from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
import bibliopixel.animation
import bibliopixel.led

class Animation(object):
    def __init__(self, step, period=4, number=80,
                driver='LPD8806', geometry='Strip', anim=None):
        ds = DriverSerial(num=number, type=getattr(LEDTYPE, driver))
        led = getattr(bibliopixel.led, 'LED' + geometry)(ds)
        led._internalDelay = period
        anim_name = 'Base' + (anim or geometry) + 'Anim'
        self.animation = getattr(bibliopixel.animation, anim_name)(led)
        self.step = step
        self.animation.step = self.step_function

    def buffer(self):
        return self.animation._led.buffer

    def step_function(self, amt=1):
        self.animation._step += 1
        self.step()

    def run(self):
        try:
            self.animation.run()
        except KeyboardInterrupt:
            pass
        except serial.SerialException:
            pass
        except e:
            print('Unhandled exception', e)
        finally:
            self.exit()

    def exit(self):
        self.animation.stopThread()
        self.animation._led.all_off()
        self.animation._led.update()
