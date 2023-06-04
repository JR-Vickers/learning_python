from functools import reduce
import math

def factorialRecursive(n):
    if n == 1:
        return n
    else:
        return n * factorialRecursive(n-1)

def factorialReduce(n):
    total = 1
    for i in list(range(n)):
      total *= i+1
    return total

def factorialReduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

def factorialLib(n):
    return math.factorial(n)

print(factorialRecursive(6))
print(factorialReduce(6))
print(factorialLib(6))