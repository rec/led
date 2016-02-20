
class Displayable(object):
    def __init__(self, name, value, format, callback=None):
        self.name = name
        self.value = value
        self.format = format
        if callback:
            self.callback = callback

    def set(self, value):
        self.value = value
        self.update()

    def serialize(self):
        return self.value

    def display(self):
        return self.format.format(name=self.name, value=self.value)

    def update(self):
        self.callback(self.display())

class Dicts(object):
    def __init__(self, *args, **kwds):
        for d in args + (kwds,):
            for k, v in d.items():
                setattr(self, k, v)


def curses_printer(screen, x, y, width, style):
    """Return a callback that prints the item to the curses screen."""
    return lambda s: screen.addscr(x, y, s[:width], style)




class Toggle(Displayable):
    def __init__(self)
