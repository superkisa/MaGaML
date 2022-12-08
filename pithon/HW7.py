"""
def retry_if_none(func):

    def obertka(*args, **kwargs):
        a = func(*args, **kwargs)
        k: int = 1
        while k != 3 and (a is None):
            a = func(*args, **kwargs)
            k += 1
        return a

    return obertka


@retry_if_none
def foo():
    print('foo')
    return None


@retry_if_none
def bar() -> int:
    print('bar')
    return 1


foo()
bar()

"""
"""
def retry_if_none(N):

    def decorator(func):

        def obertka(*args, **kwargs):
            a = func(*args, **kwargs)
            k: int = 1
            while k != N and (a is None):
                a = func(*args, **kwargs)
                k += 1
            return a

        return obertka

    return decorator


@retry_if_none(10)
def foo():
    print('foo')
    return None


@retry_if_none(10)
def bar() -> int:
    print('bar')
    return 1


foo()
bar()
"""

from typing import Any
"""
class retry_if_none():

    def __init__(self, func):
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any):
        a: Any = self.func(*args, **kwargs)
        k: int = 1
        while k != 3 and (a is None):
            a = self.func(*args, **kwargs)
            k += 1
        return a


@retry_if_none
def foo():
    print('foo')
    return None


@retry_if_none
def bar() -> int:
    print('bar')
    return 1


foo()
bar()
"""
"""
class retry_if_none():

    def __init__(self, N=3):
        self.N = N

    def __call__(self, func):

        def obertka(*args, **kwargs):
            a: Any = func(*args, **kwargs)
            k: int = 1
            while k != self.N and (a is None):
                a = func(*args, **kwargs)
                k += 1
            return a

        return obertka


@retry_if_none(10)
def foo():
    print('foo')
    return None


@retry_if_none(10)
def bar() -> int:
    print('bar')
    return 1


foo()
bar()
"""


def log_recursion_depth(func: Any):
    level: int = 0
    max_lvl: int = 1

    def wrapper(*args: Any, **kwargs: Any):
        nonlocal level, max_lvl
        level += 1
        result = func(*args, **kwargs)
        level -= 1
        if level == 0 and level < max_lvl:
            print(f'\'{func.__name__}\' function was called. recursion depth is {max_lvl}')
            max_lvl = 0
        max_lvl += 1
        return result

    return wrapper


@log_recursion_depth
def foo():
    return None


foo()


@log_recursion_depth
def factorial(factor):
    if factor == 1:
        return 1
    else:
        return factor * factorial(factor - 1)


factorial(5)

factorial(6)


@log_recursion_depth
def sum_by_parts(values: list[float]):
    if len(values) == 1:
        return values[0]
    else:
        middle = len(values) // 2
        return sum_by_parts(values[:middle]) + sum(values[middle:])


sum_by_parts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
