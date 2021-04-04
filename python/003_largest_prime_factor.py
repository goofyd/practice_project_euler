'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
n: int = 600851475143
ans = []

for i in range(2, math.ceil(math.sqrt(n))):
    while n % i == 0:
        n = int(n / i)
        ans.append(i)

print(max(ans))