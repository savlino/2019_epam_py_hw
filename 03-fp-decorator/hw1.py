
#problem1, multiples of 3 and 5
[x for x in range(1001) if x % 3 == 0 or x % 5 == 0]


#problem 6, sum square difference
sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)])


#problem9, special pythagorean triplet
[(2 * (m**5 * n - m * n**5)) for m in range(500) for n in range(500) if (m * n + m**2 == 500) and m**2 - n**2 > 0][0]


#problem40, Champernowne's constant
from functools import reduce
reduce(lambda x, y: x * y, [int(''.join([str(x) for x in range(200000)])[10**x]) for x in range(7)])


#problem48, Self powers
str(sum(n**n for n in range(1, 1001)))[-10:]
