'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
n = 1000
for a in range(0, int(n/3)):
    for b in range(0, int(n/2)):
        c = n - a - b
        cond = (a ** 2 + b ** 2) == c ** 2
        if cond:
            print('{} + {} = {}'.format(a, b, c))
            print('{} + {} = {}'.format(a**2, b**2, c**2))
            print(a*b*c)