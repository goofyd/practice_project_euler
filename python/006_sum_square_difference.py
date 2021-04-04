'''
The sum of the squares of the first ten natural numbers is,
1(square) + 2(square)+......+10(square) = 385
The square of the sum of the first ten natural numbers is,
(1+2+3+....+10)(square) = 55 (square) = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import math


def diff(start: int, end: int) -> int:
    a = int(sum([math.pow(x, 2) for x in range(start, end)]))
    b = int(math.pow(sum([x for x in range(start, end)]), 2))
    return b-a


print(diff(1, 101))