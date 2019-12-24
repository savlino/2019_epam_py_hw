"""
function is_armstrong allows to check if the given number
is one of Armstrong(narcissistic) numbers
"""

import functools


def is_armstrong(int_number):
    number = str(int_number)
    digits = [int(number[x]) for x in range(len(number))]
    dig_sum = functools.reduce(lambda x, y: x + y**len(number), digits)
    return int_number == dig_sum


assert if is_armstrong(153) is True, 'Armstrong number'
assert if is_armstrong(10) is False, 'not an Armstrong number'
