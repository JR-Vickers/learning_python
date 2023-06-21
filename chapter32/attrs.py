# Exercise 4
class Attrs:
    def __getattribute__(self, name):
        print(f"Fetching attribute: {name}")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(f"Setting attribute: {name} = {value}")
        super().__setattr__(name, value)


# Example usage
attrs = Attrs()
attrs.foo = 42  # Output: Setting attribute: foo = 42
print(attrs.foo)  # Output: Fetching attribute: foo, 42
