1.  What two operator overloading methods can you use to support iteration in your classes?
    __iter__, __next__

2.  What two operator overloading methods handle printing, and in what contexts?
    __str__ is used first for the print operation and the str built-in function.
    __repr__ is used in all other contexts.

3.  How can you intercept slice operations in a class?
    __getitem__

4.  How can you catch in-place addition in a class?
    It tries __iadd__ first, and __add__ second.

5.  When should you provide operator overloading?
    When a class naturally matches, or needs to emulate, a built-in type's interfaces.