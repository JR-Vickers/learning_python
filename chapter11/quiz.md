1.  Name three ways that you can assign three variables to the same value.
    A = B = C = 0
    A, B, C = 0, 0, 0
    A = 0, B = 0, C = 0

2.  Why might you need to care when assigning three variables to a mutable object?
    All three names reference the same object, so changing the object in one place will affect the others.

3.  What's wrong with saying L = L.sort()?
    Lists are mutable, so reassignment is unnecessary and will return None.  Simply typing L.sort() will suffice.

4.  How might you use the print operation to send text to an external file?
    print(X, file=F)  # For Python 3.X