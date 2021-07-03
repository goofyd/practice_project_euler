#print set of duplicate values

l = [1, 2, 3, 4, 4, 5, 5, 6, 1]

print(set([x for x in l if l.count(x)>1]))