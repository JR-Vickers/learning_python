# Exercise 2
class MyList:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        elif isinstance(data, MyList):
            self.data = data.data[:]
        else:
            self.data = data[:]

    def __repr__(self):
        return repr(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __add__(self, other):
        new_list = self.data[:]
        new_list += other
        return MyList(new_list)

    def append(self, item):
        self.data.append(item)

    def sort(self, *args, **kwargs):
        self.data.sort(*args, **kwargs)

# Exercise 3
class MyListSub(MyList):
    def __init__(self, data=None):
        super().__init__(data)
        self.add_counter = 0

    def __add__(self, other):
        self.add_counter += 1
        print("Performing the + operation")
        return super().__add__(other)

    def append(self, item):
        print("Appending an item to MyListSub")
        super().append(item)

    def print_counters(self):
        print("Addition Count:", self.add_counter)


# Example usage for Exercise 2
original_list = [1, 2, 3]
my_list = MyList(original_list)
print(my_list)  # Output: [1, 2, 3]

my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list += [5, 6]
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

for item in my_list:
    print(item)  # Output: 1, 2, 3, 4, 5, 6

del my_list[0]
print(my_list)  # Output: [2, 3, 4, 5, 6]

print(len(my_list))  # Output: 5

print(3 in my_list)  # Output: True

my_list.sort()
print(my_list)  # Output: [2, 3, 4, 5, 6]


# Example usage for Exercise 3
my_list_sub = MyListSub([1, 2, 3])
other_list = [4, 5]

result = my_list_sub + other_list
print(result)  # Output: [1, 2, 3, 4, 5]

my_list_sub.append(6)  # Output: Appending an item to MyListSub
print(my_list_sub)  # Output: [1, 2, 3, 6]

my_list_sub.print_counters()  # Output: Addition Count: 1