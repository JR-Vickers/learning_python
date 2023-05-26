"""
1.  What are the main functional differences between a while and a for?
    A while loop is a general looping statement; a for loop iterates through an object.

2.  What's the difference between break and continue?
    Break ends the loop immediately; continue jumps back to the top of the loop.

3.  When is a loop's else clause executed?
    When the loop's condition is False, the else clause fires.

4.  How can you code a counter-based loop in Python?
    A common choice is to assign a counter variable, and organize the while statement into something like this:

    counter = 0
    while counter < 10:
        # perform desired operation
        counter += 1

    This code will loop 10 times, until counter == 10 and the while loop stops.

5.  What can a range be used for in a for loop?
    A range can be used to repeat a function X times, for example:

    for n in range(10):
        print("Hello world!")

    This will print "Hello world!" 10 times.

"""