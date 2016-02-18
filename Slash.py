from __future__ import print_function

import curses

"""
How will the interface work?

"Out-of-the-box" there are very few hot keys.

/ always gets you to a tree of commands which is always the same:

/
  single character until you get to a final command
  executes the command if it has no parameters
  otherwise, presents a default for each parameter in an editable window
  keeps track of every command you ever did...

and you can attach commands to all "regular" keystrokes except:

escape
return
/

"""

SLASH = {
    'c': ('command', {
        'k': ('key', assign_command),
        'p': ('previous', previous),
        }),
    'h': ('help', do_help),
    'k': ('key', {
        'a': ('assign', assign),
        'c': ('clear', clear),
        'c': ('list', list_key),
        }),
    'p': ('preset', {
        'l': list_preset,
        'r': read,
        'w': write,
        }),
    'q': ('quit', do_quit),
    'r': ('redo', redo),
    'u': ('undo', undo),
    's': ('set', {
        'b': ('blackout', blackout),
        'r': ('reverse', reverse),
        's': ('speed', speed),
        }),
    't': ('transform', {
        'c': ('clear', clear),
        'p': ('permute', {
            'r': ('random', random),
            'i': ('invert', invert),
            }),
        'r': ('random', random),
        }),
    }

def read_slash(input):


if __name__ == '__main__':
    curses.wrapper(main)
