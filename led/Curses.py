from __future__ import print_function

import curses

class Color(object):
    COLORS = []

    @staticmethod
    def add_color(color):
        Color.COUNT += 1
        return Color.COUNT

    def __init__(self,
                 foreground=curses.COLOR_BLACK, background=curses.COLOR_WHITE):
        self.index = Color.next_index()
        self.set(foreground, background)

    def set(self, foreground=None, background=None):
        self.foreground = foreground or self.foreground
        self.background = background or self.background
        curses.init_pair(self.index, self.foreground, self.background)


class Style(object):
    def __init__(self, color, flags=None):
        self.color = color
        self.flags = flags


def main(screen):
    screen.clear()
    screen_y, screen_x = screen.getmaxyx()
    screen.move(1, 1)
    screen.addstr(str(screen.getmaxyx()))
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    while True:
        c = screen.getch()
        screen.move(2, 2)
        # screen.addstr(str(c), curses.A_BLINK | curses.A_BOLD)
        # screen.addstr(str(c), curses.color_pair(1))
        screen.addstr(str(c), curses.color_pair(1) | curses.A_BLINK)
        if c == 'q' or c == ord('q'):
            break

if __name__ == '__main__':
    curses.wrapper(main)
