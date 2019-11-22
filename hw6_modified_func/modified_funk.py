import inspect

def modified_func(func, fixated_args, fixated_kwargs):
    new_func = func
    new_func.__name__ = f'{func.__name__}'
    new_func.__doc__ = f"""A func implementation of {func.__name__}
with pre-applied arguments being:
{inspect.getcallargs(func)}
source_code:
{inspect.getsource(func)}
"""
    return new_func
    # if fixated_args = [] and fixated_kwargs = []:
    #     return new_func
    # else:
    #     return new_func(fixated_args, **kwargs)
