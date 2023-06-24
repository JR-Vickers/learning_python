1.  What are the two new constraints on user-defined exceptions in Python 3.X?
    They may be defined by classes.  They can must also be derived from the built-in classes.

2.  How are raised class-based exceptions matched to handlers?
    By superclass relationship.

3.  Name two ways that you can attach context information to exception objects.
    Filling out instanced attributes and by using built-in exception superclasses.

4.  Name two ways that you can specify the error message text for exception objects.
    With a custom __str__ operator and built-in exception superclasses.

5.  Why should you not use string-based exceptions anymore today?
    They have been removed as of Python 2.6 and 3.0.