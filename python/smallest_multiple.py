'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

a: int = 1
b: int = 21
n: int = 2520

while len([x for x in range(a, b) if n % x == 0]) != (b-a):
    n += 20
print(n)