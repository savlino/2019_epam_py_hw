"""
applydecorator turns decorated function to wrapper
"""


def applydecorator(*args):
    def wrapper(func, *args):
        def inner(*func_args):
            return func_args
        print(func.__name__)
        return inner
    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
