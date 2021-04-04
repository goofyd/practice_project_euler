'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


def generate_prime_numbers(n: int):
    prime_numbers = []
    for x in range(2, n):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime_numbers.append(x)
    return prime_numbers


prime_numbers = generate_prime_numbers(110000)
print(prime_numbers[10000])