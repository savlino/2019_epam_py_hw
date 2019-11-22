''' function make_it_count accepts function and counter value
returns new function with same functionality as given,
but also increments counter
'''

counter = 0
function = None


def make_it_count(func, counter_name):
    # initial function, returns function with counter incremenator
    global counter, function
    counter = counter_name
    function = func

    return my_func


def my_func(x):
    # provides result of given function and increments counter
    global counter, function
    counter += 1

    return function(x)
