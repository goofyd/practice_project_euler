'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math


def gen_prime_numbers(threshold: int):
    prime: int = 2
    prime_numbers = [True for x in range(threshold+1)]
    while prime <= threshold:
        if prime_numbers[prime]:
            for x in range(prime * 2, threshold + 1, prime):
                prime_numbers[x] = False
        prime += 1
    prime_numbers[0] = False
    prime_numbers[1] = False
    return [i for i, x in enumerate(prime_numbers) if x]


sum_prime_numbers = sum(gen_prime_numbers(2000000))
print(sum_prime_numbers)