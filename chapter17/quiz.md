1.  What is the output of the following code, and why?
X = 'Spam'
def func():
    print(X)
func() # This prints 'Spam'; func() can access the X variable since it is global.

2.  What is the output of this code, and why?
X = 'Spam'
def func():
    X = 'NI!'
func()
print(X) # This prints 'Spam!'; since 'NI!' is only accessible within func()

3.  What does this code print, and why?
X = 'Spam'
def func():
    X = 'NI'
    print(X)

func() # This statement prints 'NI', since func() contains a print statement.
print(X) # This statement prints 'Spam', since that is the value assigned to X in the global namespace.

4.  What output does this code produce?  Why?
X = 'Spam'
def func():
    global X
    X = 'NI'
    print(X)

func() # This prints 'NI', since func() renames X to 'NI'
print(X) # This also returns 'NI', since func() uses the global statement to apply the value of 'NI' to X in the global namespace.

5.  What about this code - what's the output, and why?
X = 'Spam'
def func():
    X = 'NI'
    def nested():
        print(X)
    nested()

func() # This prints 'NI', since func() assigns 'NI' to X and prints it. The additional nested function doesn't change this.
print(X) # This prints 'Spam', since func() doesn't alter X in the global namespace, only the local namespace.

6.  How about this example: what is its output in Python 3.X, and why?
def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)

func() # This prints 'Spam', since the nested() function uses the nonlocal statement to apply its definition of X to func().

7.  Name three or more ways to retain state information in a Python function.
    Using shared global variables, enclosing function scope references within nested functions, or using default argument values.