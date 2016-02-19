from __future__ import print_function

import curses

def main(screen):
    screen.clear()
    screen_y, screen_x = screen.getmaxyx()
    screen.addstr(0, 0, str(screen.getmaxyx()))
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    global DIR
    DIR = dir(screen)
    while True:
        c = screen.getch()
        screen.addstr(2, 2, str(c) + '   ', curses.color_pair(1) |
                      curses.A_BLINK | curses.A_BOLD)
        if c == 'q' or c == ord('q'):
            break

if __name__ == '__main__':
    curses.wrapper(main)
    print(DIR)
