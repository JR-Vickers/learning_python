1.  What is the difference between enclosing a list comprehension in square brackets and parentheses?
    A comprehension expressed in brackets produce the result list all at once.  A comprehension expressed in parentheses is a generator expression, which yields a generator object that yields one item in the result at a time.

2.  How are generators and iterators related?
    Generators are very similar to iterators, but their outputs are compiled specially into an object that supports the iteration protocol.

3.  How can you tell if a function is a generator function?
    It uses the yield keyword, rather than return.

4.  What does a yield statement do?
    Yield returns a result generator that can appear in any iteration context.

5.  How are map calls and list comprehensions related?  Compare and contrast the two.
    They are both iterators that perform many of the same functions, but list comprehensions tend to be much more efficient.  Maps are more versatile, however.