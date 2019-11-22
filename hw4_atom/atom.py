''' function that returns array of four functions,
defined to get, set, process and delete encapsulated value,
by default equal to 'None'
'''

the_value = None


def atom(n=None):
    # initial function, that binds functions to given Value
    global the_value
    the_value = n
    return [get_value, set_value, process_value, del_value]


def set_value(x):
    # Value setter function
    global the_value
    the_value = x


def get_value():
    # Value getter function
    global the_value
    return the_value


def process_value(*args):
    # accepts given function(s) and returns result of processing over Value
    global the_value
    for f in args:
        return f(the_value)


def del_value():
    # resets Value to default
    global the_value
    the_value = None
