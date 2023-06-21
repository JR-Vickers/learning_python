# Exercise 1
class Adder:
    def __init__(self, data=0):
        self.data = data

    def add(self, x, y):
        print("Not Implemented")

    def __add__(self, other):
        result = self.value + other.value
        return Adder(result)

class ListAdder(Adder):
    def add(x, y):
        print(x + y)

class DictAdder(Adder):
    def add(x, y):
        print({x, y})

adder = Adder()
adder.add(3,5)
ListAdder.add(3,5)
DictAdder.add(3,5)