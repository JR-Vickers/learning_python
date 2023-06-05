1.  How does a module source code file become a module object?
    It automatically becomes a module when that module is imported.

2.  Why might you have to set your PYTHONPATH environment variable?
    To import from other directories.

3.  Name the five major components of the module import search path.
    Home directory, the directories in PYTHONPATH, the standard library, all directories in .pth path files, and the site-packages root directory.

4.  Name four file types that Python might load in response to an important operation.
    source code, byte code, C extension module, or a directory of the same name for package imports.

5.  What is a namespace, and what does a module's namespace contain?
    It's a self-contained package of variables, which are known as the attributes of the namespace object.  It contains all of the names assigned by code at the top level of the module.