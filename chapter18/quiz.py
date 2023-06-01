"""
1.  What is the output of the following code, and why?
def func(a, b=4, c=5):
    print(a, b, c)

func(1, 2) # This prints 1 2 5, since the first two elements map onto the first two inputs in func.

2.  What is the output of this code, and why?
def func(a, b, c=5):
    print(a, b, c)

func(1, c=3, b=2) # This prints 1 2 3, since this is the order specified within func.

3.  How about this code: What is its output, and why?
def func(a, *pargs):
    print(a, pargs)

func(1, 2, 3) # This prints 1 (2, 3), since *pargs compresses all additional args into parentheses.

4.  What does this code print, and why?
def func(a, **kargs):
    print(a, kargs)

func(a=1, c=3, b=2) # This prints 1 {'c': 3, 'b': 2}, because func() first prints a, followed by the additional inputs converted into key-value pairs in a dictionary.

5.  What gets printed by this, and why?
def func(a, b, c=3, d=4): print(a, b, c, d)

func(1, *(5, 6)) # This prints 1 5 6 4, because inputs 2 and 3 are mapped onto the second and third inputs for func().  An argument for d is not provided, so it defaults to 4.

6.  One last time: what is the output of this code, and why?
def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'

l=1; m=[1]; n={'a':0}
func(l, m, n)
l, m, n 
# This displays (1, ['x'], {'a': 'y'}); the first assignment in the function doesn't impact the caller, but the second two do because they change passed-in mutable objects in place.
"""