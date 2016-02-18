from __future__ import absolute_import, division, print_function, unicode_literals

from importlib import import_module

def import_function(classpath):
    # Try to import a function out of a module.
    parts = classpath.split('.')
    function = parts.pop()

    return getattr(import_module('.'.join(parts)), function)

def importer(classpath):
    try:
        # Try to import a module.
        return import_module(classpath)
    except ImportError:
        return import_function(classpath)
