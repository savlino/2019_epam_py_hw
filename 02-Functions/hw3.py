"""
function make_it_count accepts function and counter value
returns new function with same functionality as given,
but also increments counter
"""

counter = 0
div_counter = 0
sum_counter = 0


def make_it_count(func, counter_name, *args):
    def inner_for_count(*args):
        def inner(*args):
            globals()[counter_name] += 1
            return func
        return [inner(args)]

    if args:
        arr_to_return = [inner_for_count]
        for i in args:
            ind = args.index(i)
            if ind % 2 != 0:
                continue
            arr_to_return.append(make_it_count(args[ind], args[ind + 1]))
        return arr_to_return

    return inner_for_count


def dbl(n):
    return n * 2


def div(n):
    return n / 2


def sum_(n):
    return n + 1


new_func, sec_func, th_func = make_it_count(
    dbl, 'counter', div, 'div_counter', sum_, 'sum_counter'
)

new_func(4)
new_func(4)
new_func(4)
new_func(4)
sec_func(6)
sec_func(6)
sec_func(4)
th_func(9)

assert counter == 4
assert div_counter == 3
assert sum_counter == 1
