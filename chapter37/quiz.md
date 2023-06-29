1.  What are the names and roles of string object types in Python 3.X?
    str - used for text
    bytes, bytearray - used for binary data

2.  What are the names and roles of string object types in Python 2.X?
    str - used for text and binary data
    unicode - advanced forms of text whose character sets don't map to 8-bit bytes

3.  What is the mapping between 2.X and 3.X string types?
    2.X's str equates to both str and bytes in 3.X
    3.X's str equates to both str and unicode in 2.X

4.  How do Python 3.X's string types differ in terms of operations?
    bytes are actually short integers, though Python tries to present them as characters when possible.  This means that when using the '+' operator on two byte objects, it will return the sum of two integers.  In contrast, the '+' operator used on a pair of str objects concatenates them.

5.  How can you code non-ASCII Unicode characters in a string in 3.X?
    Hex or Unicode escapes to embed Unicode code point ordinal values in text strings.

6.  What are the main differences between text- and binary-mode files in Python 3.X?
    Text files interpret file contents according to a Unicode encoding.
    Binary files return file contents to you raw, as a sequence of integers representing byte values.

7.  How would you read a Unicode text file that contains text in a different encoding than a default for your platform?
    Pass the name of the file's encoding to the open built-in in 3.X.

8.  How can you create a Unicode text file in a specific encoding format?
    Pass the encoding name to open in 3.X.

9.  Why is ASCII text considered to be a kind of Unicode text?
    It's 7-bit range of values is a subset of most Unicode encodings.

10. How large an impact does Python 3.X's string types change have on your code?
    Depends on the types of strings you use.  For scripts that use simple ASCII text on platforms with ASCII-compatible default encodings, the impact is minor.