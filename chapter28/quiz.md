1.  When we fetch a Manager object from the shelve and print it, where does the display format logic come from?
    The inheritance search climbs to its superclass.

2.  When we fetch a Person object from a shelve without importing its module, how does the object know that it has a giveRaise method that we can call?
    Shelves automatically relink an instance to the class it was created from when that instance is later loaded back into memory.

3.  Why is it so important to move processing into methods, instead of hardcoding it outside the class?
    This reduces code redundancy and complexity.

4.  Why is it better to customize by subclassing rather than copying the original and modifying?
    Because this would introduce redundant code, and any changes made to the original would fail to carry over to the copy.

5.  Why is it better to call back to a superclass method to run default actions, instead of copying and modifying its code in a subclass?
    It reduces redundancy and conflicts.

6.  Why is it better to use tools like __dict__ that allow objects to be process generically than to write more custom code for each type of class?
    They can avoid hardcoded solutions that must be kept in sync with the rest of the class as it evolves over time.

7.  In general terms, when might you choose to use object embedding and composition instead of inheritance?
    Inheritance is best at coding extensions based on direct customization.  Composition is well suited to scenarios where multiple objects are aggregated into a whole and directed by a controller layer class.

8.  What would you have to change if the objects coded in this chapter used a dictionary for names and a list for jobs, as in similar examples earlier in this book?
    The lastName method would need to be updated for the new name format, the Person constructor would have to change the job default to an empty list, and the Manager class would probably need to pass along a job list in its constructor instead of a single string.

9.  How might you modify the classes in this chapter to implement a personal contacts database in Python?
    You can modify the attributes to contain the desired information.  You can also add whatever methods are relevant.