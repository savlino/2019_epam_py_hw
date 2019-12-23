"""
function that returns array of four functions,
defined to get, set, process and delete encapsulated value,
by default equal to 'None'
when more than one argument passed to 'atom',
functions' names (set of 4) for operating over 2nd and next variables
should be wrapped in list separately, as such:
get_1, set_1, proc_1, del_1, \
[get_2, get_2, proc_2, del_2], ... = atom(1, 2, ...)
"""


def atom(n=None, *args):
    # initial function, that binds functions to given Value
    the_value = None

    if n:
        the_value = n

    def get_value():
        # Value getter function
        return the_value

    def set_value(x):
        # Value setter function
        nonlocal the_value
        the_value = x
        print(f'value is {x} now')

    def process_value(*args):
        # accepts given function(s) and returns result of processing over Value
        for f in args:
            print(f(the_value))

    def del_value():
        # resets Value to default
        nonlocal the_value
        the_value = None

    if args:
        if len(args) > 1:
            ret_funcs = [get_value, set_value, process_value, del_value]
            for t in args:
                ret_funcs.append(atom(t))
            return ret_funcs
        else:
            return [
                get_value, set_value, process_value, del_value, atom(args[0])
            ]
    return [get_value, set_value, process_value, del_value]
