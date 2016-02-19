from __future__ import print_function

from collections import OrderedDict

from . Importer import import_function

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
    'command': {
        'key': ('key', assign_command),
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


def call(name, args, kwds):
    function = import_function(name)
    return lambda x: function(*args, **kwds)

def to_function(data):
    assert data
    if instanceof(data, str):
        # It's a function.
        data = data[1:] if data.startswith('.') else namespace + data
        return import_function(data)

    assert instanceof(data, (list, tuple))
    # It's a maker of functions.
    data = list(data)
    len(data) < 2 and data.append([])
    len(data) < 3 and data.append({})
    assert(len(data) == 3)
    name, args, kwds = data
    args = args or []
    kwds = kwds or {}
    if not isinstance(args, (list, tuple)):
        args = [args]

    return import_function(name)(*args, **kwds)


def read(data, namespace):
    assert data
    if isinstance(data, dict):
        return OrderedDict((k, read(v, namespace)) for (k, v) in data.items()}
    else:
        return to_function(data)
