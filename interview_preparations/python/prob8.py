def search(a, n):
    if n in a:
        return a.index(n)
    return -1

l = [x**2 for x in range(10)]
print(search(l, 4))


print(True + True +10)
a = [1,2,3,4,5]
#print(a[5])

print('key1' in {'key2':22, 'key1':12})

i = 20

def up():
    #global i
    i=100
    print(i+120)

print(i)
s = up()
print(s)

c = ['a', 'c', 'd']
d = ['b', 'a', 'f']
print(d>c)