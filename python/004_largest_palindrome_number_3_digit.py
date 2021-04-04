'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

max_value = []
a: int = 100
b: int = 1000


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def get_largest_palindrome(lower: int, higher: int) -> int:
    for x in range(lower, higher):
        for y in range(lower, higher):
            prod = x * y
            if is_palindrome(str(prod)):
                max_value.append(prod)
    return max(max_value)


print(get_largest_palindrome(a, b))