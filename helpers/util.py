from functools import wraps
from time import time


def timed_f(func):
    @wraps(func)
    def _timed(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return _timed

