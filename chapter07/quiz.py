"""
1.  Can the string find method be used to search a list?
    No.

2.  Can a string slice expression be used on a list?
    Nope.

3.  How would you convert a character to its ASCII integer code?  How would you conver the other way, from an integer to a character?
    ord(S)
    chr(I)

4.  How might you go about changing a string in Python?
    Strings are immutable, so you'd have to redefine the string.  For example, if you wanted to change the contents of a string to uppercase, you could do something like this:
    myStr = "hello world"
    myStr = myStr.upper()
    print(myStr) # this would print 'HELLO WORLD'

5.  Given a string S with the value "s,pa,m", name two ways to extract the two characters in the middle.
    S.split(",")[1]
    S[slice(2, 4)]

6.  How many characters are there in the string "a\nb\x1f\000d"?
    6

7.  Why might you use the string module instead of string method calls?
    You wouldn't, since it's deprecated.

"""