# The exercise is to explain what is going on in the following expressions.

2 ** 16                                     # outputs 2 to the 16th power, 65,536
2 / 5, 2 / 5.0                              # Divides 2 by 5, first with 5 as an integer, then with 5 as a float.  In both cases, the output is converted into a float, 0.4

"spam" + "eggs"                             # string concatenation, 'spameggs'
S = "ham"                                   # variable assignment
"eggs" + S                                  # more string concatenation, this time using a variable.  Outputs 'eggsham'
S * 5                                       # outputs 'ham' 5 times
S[:0]                                       # selects the whole string up to index 0 (noninclusive).  Since index 0 is the start of the string, it outputs an empty string ''
"green %s and %s" % ("eggs", S)             # splices "eggs" and S into the string, outputting 'green eggs and ham'
'green {0} and {1}'.format('eggs', S)       # same thing with alternate syntax

('x',)[0]                                   # creates tuple containing 'x', then outputs it
('x', 'y')[1]                               # creates tuple 'x', 'y', then returns 'y'

L = [1,2,3] + [4,5,6]                       # Creates list L = [1, 2, 3, 4, 5, 6]
L, L[:], L[:0], L[-2], L[-2:]               # Outputs four items: the original list L, a copy of list L, an empty string '', 5, and the last two items in the list [5, 6]
([1,2,3] + [4,5,6])[2:4]                    # Combines two lists, the returns the items from index 2 to 4 (noninclusive), resulting in [3, 4]
[L[2], L[3]]                                # Also returns [3, 4], but more cleanly.
L.reverse(); L                              # Reverses L and returns it.
L.sort(); L                                 # This sorts L and returns it, undoing the previous step.
L.index(4)                                  # Returns 3