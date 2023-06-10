1.  What is the main point of OOP in Python?
    It allows for an often more effective way of programming in which we factor code to reduce redundancy and write new programs by customizing existing code instead of changing it in place.

2.  Where does an inheritance search look for an attribute?
    In the specified class.

3.  What is the difference between a class object and an instance object?
    A class is an instance factory.  Their attributes provide behavior that is inherited by all the instances generated from them.
    Instances represent the concrete items in a program's domain.

4.  Why is the first argument in a class's method function special?
    Python passes in the implied instance to a special first argument in the method, called self by convention.

5.  What is the __init__ method used for?
    If it's coded or inherited, Python automatically calls __init__ each time an instance is generated from a class.  The new instance is passed in to the self argument of __init__ as usual, and any values listed in parentheses in the class call go to arguments two and beyond.  The effect is to initialize instances when they are made, without requiring extra method calls.

6.  How do you create a class instance?
    By calling the class name as though it were a function.

7.  How do you create a class?
    Run a class statement.

8.  How do you specify a class's superclasses?
    By listing them in parentheses in the class statement, after the new class's name.