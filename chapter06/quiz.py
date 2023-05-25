"""
1.  Consider the following three statements.  Do they change the value printed for A?
    A = "spam"
    B = A
    B = "shrubbery"

    No, they do not.

2.  Consider these three statements.  Do they change the printed value of A?
    A = ["spam"]
    B = A
    B[0] = "shrubbery"

    Yes, A returns ["shrubbery"]

3.  How about these - is A changed now?
    A = ["spam"]
    B = A[:]
    B[0] = "shrubbery"

    No, A is not changed.
"""