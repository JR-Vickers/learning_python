1.  How do you make a module?
    Any file ending in .py can be used as a module.

2.  How is the from statement related to the import statement?
    from allows you to import specific names from modules, allowing more direct access.

3.  How is the reload function related to imports?
    It allows you to re-import a module.  Typically, modules are only imported once, since imports are so computationally expensive.

4.  When must you use import instead of from?
    When you must use the same name defined in two different modules.

5.  Name three potential pitfalls of the from statement?
    It can obscure the meaning of a variable, can have problems with the reload call, and can corrupt namespaces.