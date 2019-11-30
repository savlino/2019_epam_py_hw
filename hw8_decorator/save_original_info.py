import functools


def save_info(inner):
    def super_wrap(wrap_func):
        def wrapped(*args, **kwargs):
            wrapped.__name__ = "custom_sum"
            wrapped.__doc__ = \
                """This function can sum any objects which have __add___"""
            wrapped.__original_func = inner
            return wrap_func(*args, **kwargs)
        return wrapped
    return super_wrap


def print_result(func):
    @save_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
