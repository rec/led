from __future__ import print_function

from . import Serialize

import json

PRESET_FILE = '.presets'

class Presets(object):
    def __init__(self, preset_size=10):
        try:
            fp = open(PRESET_FILE)
        except:
            self.presets = preset_size * [None]
        else:
            self.presets = json.load(fp)
        while len(self.presets) < preset_size:
            self.presets.append(None)

    def preset(self, i):
        preset = self.presets[i]
        if preset:
            print('Loaded preset', i)
            return preset
        print('No preset stored at', i)

    def set_preset(self, i, data):
        self.presets[i] = Serialize.serialize(data)
        json.dump(self.presets, open(PRESET_FILE, 'w'))
        print('Stored preset at', i)
