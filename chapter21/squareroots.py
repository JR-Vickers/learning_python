import math
values = [2, 4, 9, 16, 25]

def squarerootsFor(arg):
    roots = []
    for n in arg:
        roots.append(math.sqrt(n))
    return roots

def squarerootsMap(arg):
    return list(map(math.sqrt, arg))

def squarerootsComp(arg):
    return [math.sqrt(x) for x in arg]

def squarerootsGen(arg):
    return (math.sqrt(x) for x in arg)

print(squarerootsFor(values))
print(squarerootsMap(values))
print(squarerootsComp(values))
for num in squarerootsGen(values):
    print(num, end=", ")