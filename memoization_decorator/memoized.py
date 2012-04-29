import functools

def memoized(func):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated."""
    cache = {}

    @functools.wraps(func)
    def memoizer(*args, **kwargs):
        #keywords = tuple(sorted(kwargs.iteritems()))
        keywords = tuple(kwargs.iteritems())
        key = (args, keywords)
        try:
            return cache[key]
        except KeyError:
            value = func(*args, **kwargs)
            cache[key] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return func(*args, **kwargs)

    memoizer.cache = cache
    return memoizer
