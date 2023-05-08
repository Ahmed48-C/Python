# Nested Dictionaries and Lists

# Modeling a tic-tac-toe board was fairly simple: the board needed only a single dictionary value with nine key-value pairs. 
# As you model more complicated things, you may find you need dictionaries and lists that contain other dictionaries and lists.
 
# Lists are useful to contain an ordered series of values, and dictionaries are useful for associating keys with values. 
# For example, here’s a program that uses a dictionary that contains other dictionaries of what items guests are bringing to a picnic. 

# The totalBrought() function can read this data structure and calculate the total number of an item being brought by all the guests.

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

# Inside the totalBrought() function, the for loop iterates over the key-value pairs in guests ➊. 
# Inside the loop, the string of the guest’s name is assigned to k, and the dictionary of picnic items they’re bringing is assigned to v. 
# If the item parameter exists as a key in this dictionary, its value (the quantity) is added to numBrought ➋. 
# If it does not exist as a key, the get() method returns 0 to be added to numBrought.

# The output of this program looks like this:

#  Number of things being brought:
#  - Apples 7
#  - Cups 3
#  - Cakes 0
#  - Ham Sandwiches 3
#  - Apple Pies 1

# This may seem like such a simple thing to model that you wouldn’t need to bother with writing a program to do it.
# But realize that this same totalBrought() function could easily handle a dictionary that contains thousands of guests,
# each bringing thousands of different picnic items. 
# Then having this information in a data structure along with the totalBrought() function would save you a lot of time!

# You can model things with data structures in whatever way you like, as long as the rest of the code in your program can work with the data model correctly. 
# When you first begin programming, don’t worry so much about the “right” way to model data. 
# As you gain more experience, you may come up with more efficient models, 
# but the important thing is that the data model works for your program’s needs.