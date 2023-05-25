L = [1, 2, 3, 4]
L[2] = []                   # This changes L to [1, 2, [], 4]
L[2:3] = []                 # This changes L to [1, 2, 4]
del L[0]; L                 # Deletes L[0], returning [2, 4]
del L[1:]; L                # Deletes everything from index 1 (inclusive) to the end; returns [2]
L[1:2]=1                    # error