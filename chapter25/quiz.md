1.  What is significant about variables at the top level of a module whose names begin with a single underscore?
    Variables whose names begin with a single underscore are not copied out to the importing scope when the from * statement form is used.

2.  What does it mean when a module's __name__ variable is the string "__main__"?
    This is the module that stores code written at the interactive prompt.

3.  If the user interactively types the name of a module to test, how can your code import it?
    You can use exec or pass the string name in a call to the __import__ or importlib.import_module

4.  How is changing sys.path different from setting PYTHONPATH to modify the module search path?
    It only affects one running programm, and is temporary.

5.  If the module __future__ allows us to import from the future, can we also import from the past?
    Nope.