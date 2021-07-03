#print prime numbers between 100 to 200

def print_prime_numbers(start, end):
    for i in range(start, end):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count+=1
        if count == 0:
            print(i, end=", ")

def print_prime_using_all(start, end):
    for i in range(start, end):
        if all(i%x!=0 for x in range(2,i)):
            print(i, end=", ")

print_prime_using_all(100, 200)
print()
print_prime_numbers(100, 200)