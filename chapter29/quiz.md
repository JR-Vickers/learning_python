1.  What is an abstract superclass?
    A class that expects parts of its behavior to be provided by its subclasses.

2.  What happens when a simple assignment statement appears at the top level of a class statement?
    The assignment creates a name in the class's local scope, which become attributes in the associated class object.

3.  Why might a class need to manually call the __init__ method in a superclass?
    If it defines an __init__ constructor of its own and still wants the superclass's construction code to run.

4.  How can you augment, instead of completely replacing, an inherited method?
    Redefine it in a subclass, but call back to the superclass's version of the method manually from the new version of the method in the subclass.

5.  How does a class's local scope differ from that of a function?
    It does not serve as an enclosing local scope to further nested code.