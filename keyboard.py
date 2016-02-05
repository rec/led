from __future__ import absolute_import, division, print_function, unicode_literals

# From https://stackoverflow.com/questions/9865446

import termios, fcntl, sys, os, threading

def keyboard(callback):
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:
        while True:
            try:
                callback(sys.stdin.read(1))
            except IOError:
                pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def threaded(callback, **kwds):
    t = threading.Thread(target=lambda: keyboard(callback), **kwds)
    t.start()
    return t

if __name__ == '__main__':
    threaded(lambda c: print('Keystroke ' + c))
