from __future__ import print_function

class FlipFlop(object):
    def __init__(self, name, state=False, display_name=None):
        self.name = name
        self.display_name = display_name or name
        self.state = False

    def change(self, state=None):
        if state is not self.state:
            self.state = not self.state if state is None else state
            if self.state:
                print(self.display_name)
            else:
                print('not', self.display_name)

    def __nonzero__(self):
        return self.state
