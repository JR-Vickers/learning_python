S = 'spam'
S[0][0][0][0][0]            # This returns 's'.  It returns S[0] since strings are just collections of characters, and characters are just one-character strings.
S = ['s', 'p', 'a', 'm']
S[0][0][0][0][0]            # Same result