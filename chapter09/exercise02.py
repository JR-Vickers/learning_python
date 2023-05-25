# For this exercise, we'll be experimenting with boundary cases.
L = [1, 2, 3, 4]
L[4]                    # This gives a traceback error
L[-1000:100]            # This doesn't do anything, it just returns L
L[3:1]                  # This returns an empty list.  It starts at index 3, but can't move back to index 1.