from __future__ import print_function

import curses

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
