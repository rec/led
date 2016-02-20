import inspect

def serialize(x):
    if isinstance(x, (basestring, bool, float, int, long, type(None))):
        return x

    if isinstance(x, dict):
        return {k: serialize(v) for (k, v) in x.items()}

    if isinstance(x, (list, tuple)):
        return [serialize(i) for i in x]

    method = getattr(x, 'serialize', None)
    if method:
        return serialize(method())

    keys = inspect.getargspec(x.__init__).args[1:]
    return {k: serialize(getattr(x, k)) for k in keys}
