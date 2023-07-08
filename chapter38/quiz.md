1.  How do __getattr__ and __getattribute__ differ?
    __getattr__ is used for fetches of undefined attributes only.  __getattribute__ works whether the attributes are defined.

2.  How do properties and descriptors differ?
    Properties are specific, descriptors are generic.

3.  How are properties and decorators related?
    Properties and decorators use the same syntax.

4.  What are the main functional differences between __getattr__ and __getattribute__ and properties and descriptors?
    __getattr__ and __getattribute__ are generic; properties and descriptors provide access for only a specific attribute.