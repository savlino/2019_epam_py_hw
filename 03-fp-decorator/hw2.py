import functools


def is_armstrong(int_number):
    number = str(int_number)
    digits = [int(number[x]) for x in range(len(number))]
    dig_sum = functools.reduce(lambda x, y: x + y**len(number), digits)
    return int_number == dig_sum


assert is_armstrong(153) == True, 'Armstrong number'
assert is_armstrong(10) == False, 'not an Armstrong number'
