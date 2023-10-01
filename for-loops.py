#What?  A for loop is a control flow structure in Python used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects.
#When?  When you have specific items to iterate over.  doing specific operations on certain collections of data
#Why?  Effeciency(efficient and concise for known number of iterations), Reduce code repitition (automating the process of performing the same action on multiple items.)
#Why?  Improve readability(clear and structured way to iterate over elements).
# Creating a list of friends
friends = ["David", "Joe", "Mark", "Jason", "Robert"]

# Getting the length of the 'friends' list
len(friends)
# The above line calculates the length but does not do anything with it.

# Looping over a range of values (0, 1, 2)
for index in range(3):
    # Checking if the current index is 0
    if index == 0:
        print("You are first")  # If so, print "You are first"
    else:
        print("You are not first")  # If not, print "You are not first"
