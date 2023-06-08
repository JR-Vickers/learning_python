1.  What is the purpose of an __init__.py file in a module package directory?
    It serves to declare and initialize a regular module package.

2.  How can you avoid repeating the full package path every time you reference a package's content?
    Use the from statement to copy names out of a package.

3.  Which directories require __init__.py files?
    Directories named within the path of a package import statement.

4.  When must you use import instead of from with packages?
    Only if you need to access the same name defined in more than one path.

5.  What is the difference between from mypkg import spam and from . import spam?
    The first is an absolute import, the second is a relative import.

6.  What is a namespace package?
    An extension to the import model.