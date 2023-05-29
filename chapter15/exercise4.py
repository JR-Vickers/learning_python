X = 5
powX = 2 ** X
L = []

for i in range(7):
    L.append(2 ** i)

if 2 ** X in L:
    print(L[X], "at index", L.index(2 ** X))
else:
    print(X, "not found")