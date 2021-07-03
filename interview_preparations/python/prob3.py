#fibonacci series

def fib(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
        print(b, end=" ")

fib(12)

print()
#optimized one

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return F(n-2) + F(n-1)

for x in range(14):
    print(F(x), end=" ")