import functools

def memoized(func):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated."""
    cache = {}

    @functools.wraps(func)
    def memoizer(*args, **keywords):
        keywords = tuple(sorted(keywords.iteritems()))
        key = (args, keywords)
        try:
            return cache[key]
        except KeyError:
            value = func(*args, **keywords)
            cache[key] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return func(*args, **keywords)

    memoizer.cache = cache

