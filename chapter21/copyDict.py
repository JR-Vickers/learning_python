def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

print(copyDict({1:'a', 2:'b'}))