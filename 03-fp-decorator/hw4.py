'''applydecorator wraps decorating function'''


def applydecorator(*args):
    def wrapper(func, *args):
        def inner(*func_args):
            return func_args
        return inner
    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
