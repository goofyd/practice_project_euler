#sort the elements in a list

l = [23, 35, 56, 32, 54, 2, 54, 67, 85, 36, 85]

#inbuild method
print(sorted(l))
print(sorted(l, reverse=True))

#sort the list without using sorted function
lcopy = l.copy()
ll = []

while lcopy:
    minimum = lcopy[0]
    for x in lcopy:
        if x < minimum:
            minimum = x
    ll.append(minimum)
    lcopy.remove(minimum)

print(ll)


#sort with single loop with min() and selection sort
lcopy = l.copy()
ll = []
for x in range(len(lcopy)):
    minVal = min(lcopy)
    ll.append(minVal)
    lcopy.remove(minVal)

print(ll)

#bubble sort
lcopy = l.copy()
for x in range(len(lcopy)):
    for y in range(len(lcopy)-x-1):
        if lcopy[y] > lcopy[y+1]:
            lcopy[y], lcopy[y+1] = lcopy[y+1], lcopy[y]

print(lcopy)

#selection sort
lcopy = l.copy()
for x in range(len(lcopy)-1):
    minimum = x
    for y in range(x+1, len(lcopy)):
        if lcopy[y] < lcopy[minimum]:
            minimum = y
    lcopy[minimum], lcopy[x] = lcopy[x], lcopy[minimum]

print(lcopy)

print("**********")
lcopy = l.copy()
#recursive bubble sort
def bubbleSort(a, i):
    if i == 1:
        return
    for x in range(len(a)-1):
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]
    print(a)
    bubbleSort(a, i-1)

bubbleSort(lcopy, len(lcopy))