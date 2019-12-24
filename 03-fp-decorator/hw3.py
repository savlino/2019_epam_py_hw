"""
function accepts integer and returns number of iteration
to descend through Syracuse sequence down to 1
"""


def collatz_steps(number):
    assert type(number) == int, 'shoud be integer'
    assert number >= 0, 'shoud be positive'
    
    def loop(cntr, n):
        if n == 1:
            return cntr
        cntr = cntr + 1
        if n % 2 == 0:
            return loop(cntr, n / 2)
        elif n % 2 == 1:
            return loop(cntr, n * 3 + 1)
    return loop(0, number)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
