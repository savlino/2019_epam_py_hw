"""
module defines profile decorator for comparing function performance
and executes different ways to calculate items in Fibonacci sequence
for figuring out the fastest
"""

import time
from random import randint
import numpy as np
from math import sqrt

loop_var = None
rec_var = None
gen_var = None
mem_var = None
class_mem_var = None
matr_var = None
binet_var = None


def prof_decorator(prof_var):
    def profiler(func):
        def wrapper(*args, **kwargs):
            k = globals()[prof_var]
            if k is None:
                k = [0, 0]
            start_time = time.time()
            ret_runc = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            k[0] += 1
            k[1] += elapsed_time
            globals()[prof_var] = k
            return ret_runc
        return wrapper
    return profiler


@prof_decorator('loop_var')
def loop_fib(n):
    '''simple fibonacci function through loops'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@prof_decorator('rec_var')
def recursive_fib(n):
    '''fibonacci function using recursion'''
    if n == 1 or n == 2:
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)


@prof_decorator('gen_var')
def generator_fib(n):
    '''fibonacci using generator'''
    def inner_fib():
        a, b = 0, 1

        def fib_iter():
            while True:
                a, b = b, a + b
                yield a
        return fib_iter
    for i in range(n):
        res = inner_fib()
    return res


@prof_decorator('mem_var')
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
@prof_decorator('class_mem_var')
def class_memoize_fib(n):
    '''memoizing fibonacci function through memoize as class'''
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


@prof_decorator('matr_var')
def matrices_fib(n):
    e1 = np.array([[1, 1], [1, 0]])
    res = np.array([[1, 1], [1, 0]])
    i = 2
    while i < n:
        i += 1
        res = np.dot(e1, res)
    return res[0][0]


@prof_decorator('binet_var')
def binet_fib(n):
    p = (1 + sqrt(5)) / 2
    return round((p ** n - (-p) ** (-n)) / (2 * p - 1))


for i in range(10000):
    ind = randint(1, 25)
    loop_fib(ind)
    if rec_var is None or rec_var[0] < 10000:
        recursive_fib(ind)
    generator_fib(ind)
    memoize_fib(loop_fib, ind)
    class_memoize_fib(ind)
    matrices_fib(ind)
    binet_fib(ind)

results = {
    'loop': loop_var[1] / loop_var[0],
    'recursion': rec_var[1] / rec_var[0],
    'generator': gen_var[1] / gen_var[0],
    'memoize': mem_var[1] / mem_var[0],
    'memoize via class': class_mem_var[1] / class_mem_var[0],
    'matrices': matr_var[1] / matr_var[0],
    'Binet formula': binet_var[1] / binet_var[0]
}

fastest_func = None

for r in results:
    if not fastest_func:
        best = results[r]
    if results[r] <= best:
        best = results[r]
        fastest_func = r
    print(f'function {r} has executed \
for avg time {results[r]}')

print(f'best option for fibonacci is {fastest_func}')
