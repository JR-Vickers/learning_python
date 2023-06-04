def addDict(dict1, dict2):
    new = {}
    for key in dict1.keys():
        new[key] = dict1[key]
    for key in dict2.keys():
        new[key] = dict2[key]
    return new

print(addDict({1:'a', 2:'b'}, {2:'b', 3:'c', 4:'d'}))