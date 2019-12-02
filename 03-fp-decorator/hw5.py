'''module defines profile decorator for comparing function performance
and executes different ways to calculate items in Fibonacci sequence
for figuring out the fastest'''

import time
from random import randint

results = {}


def prof_decorator(prof_var):
    def profiler(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            ret_runc = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            if func.__name__ not in prof_var:
                prof_var[func.__name__] = [0, 0]
            prof_var[func.__name__][0] += 1
            prof_var[func.__name__][1] += elapsed_time
            return ret_runc
        return wrapper
    return profiler


@prof_decorator(results)
def loop_fib(n):
    '''simple fibonacci function through loops'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@prof_decorator(results)
def recursive_fib(n):
    '''fibonacci function using recurtion'''
    if n == 1 or n == 2:
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)


@prof_decorator(results)
def generator_fib(n):
    '''fibonacci using generator'''
    def inner_fib():
        a, b = 0, 1

        def fib_iter():
            # global a,b
            while True:
                a, b = b, a + b
                yield a
        return fib_iter
    for i in range(n):
        res = inner_fib()
    return res


@prof_decorator(results)
def memoize_fib(func, arg):
    '''fibonacci function memoizing results'''
    memo = {}
    if arg not in memo:
        memo[arg] = func(arg)
    return memo[arg]


class Memoize:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.func(arg)
        return self.memo[arg]


@Memoize
@prof_decorator(results)
def class_memoize_fib(n):
    '''memoizing fibonacci function through memoize as class'''
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


for i in range(10000):
    ind = randint(1, 20)
    loop_fib(ind)
    recursive_fib(ind)
    generator_fib(ind)
    memoize_fib(recursive_fib, ind)
    class_memoize_fib(ind)

fastest_func = None

for r in results:
    best = 1
    if results[r][1] < best:
        fastest_func = r
    print(f'function {r} has executed \
for avg time {results[r][1] / results[r][0]}')

print(f'best option for fibonacci is {fastest_func}')
