import json

def serialize(x):
    return getattr(x, 'serialize', lambda: x)()

class Serializable(object):
    _BASE_IGNORE = ('serialize', 'deserialize')
    _IGNORE = ()

    def _ignore(self, k):
        return k.startswith('_') or k in self._BASE_IGNORE or k in self._IGNORE

    def serialize(self):
        return {k: serialize(v)
                for (k, v) in self.__dict__.items()
                if not self._ignore(k)}

    @staticmethod
    def default(c):
        attr = getattr(c, 'serialize', None)
        if not attr:
            raise TypeError(repr(c) + ' is not JSON serializable')
        return attr()
