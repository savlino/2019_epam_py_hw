"""
modified_func is a wraps function winth given args and kwargs
and returns new function with same
it also allows to add args and kwargs to process them through function
"""

import inspect


def modified_func(func, fixated_args, fixated_kwargs):
    def inner(*args, **kwargs):
        print(func.__name__)
        if args:
            for m in args:
                fixated_args.append(m)
        if kwargs:
            for k in kwargs:
                fixated_kwargs[k] = kwargs[k]

        return func(*fixated_args, **fixated_kwargs)

    inner.__name__ = f'{func.__name__}'
    inner.__doc__ = f"""A func implementation of {func.__name__}
with pre-applied arguments being:
{fixated_args, fixated_kwargs}
source_code:
{inspect.getsource(func)}
"""
    return inner
