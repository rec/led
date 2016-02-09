class Saveable(object):
    _BASE_IGNORE = ('serialize', 'deserialize')
    _IGNORE = ()

    def _ignore(self, k):
        return k.startswith('_') or k in self._BASE_IGNORE or k in self._IGNORE

    def serialize(self):
        return {k: v for (k, v) in self.__dict__.items() if not self._ignore(k)}
