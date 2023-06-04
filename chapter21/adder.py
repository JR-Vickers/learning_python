def adder(*args):
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

print(adder(1, 2, 3))
print(adder("hello", "world"))
print(adder([1, 2, 3], [4, 5, 6]))
print(adder({1:'a', 2:'b'}))

# Exercise 2: Yes, you need to add print statements to see the results in the terminal.
# Exercise 3: It doesn't like it when you pass in args of different types.  It doesn't send an error message for dictionaries, but it doesn't modify them.
