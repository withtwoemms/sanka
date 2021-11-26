from typing import Callable
from typing import TypeVar


T = TypeVar('T')

class Sanka:

    def __init__(self, func: Callable, callback: Callable[[int], T] = None):
        if callback and not callable(callback):
            raise TypeError(f'Callback must be Callable not "{type(callback).__name__}"')

        self.func = func
        self.call_count = 0
        self.callback = callback

    def __call__(self, *args, **kwargs):
        if YaDead in args:
            return self.call_count

        self.call_count += 1
        if self.callback:
            self.callback(self.call_count)
        return self.func(*args, **kwargs)


def sanka(function: Callable = None, callback: Callable[[int], T] = None):
    if function:
        return Sanka(function)
    else:
        def wrapper(function):
            return Sanka(function, callback)
        return wrapper


class YaDead:
    pass

