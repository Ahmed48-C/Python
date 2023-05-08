# The setdefault() Method
# You’ll often have to set a value in a dictionary for a certain key only if that key does not already have a value. 
# The code looks something like this:

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# The setdefault() method offers a way to do this in one line of code. 
# The first argument passed to the method is the key to check for, 
# and the second argument is the value to set at that key if the key does not exist. If the key does exist, 
# the setdefault() method returns the key’s value. Enter the following into the interactive shell:
'''
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
'''

# The first time setdefault() is called, the dictionary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}.
# The method returns the value 'black' because this is now the value set for the key 'color'. 
# When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white', 
# because spam already has a key named 'color'.

# The setdefault() method is a nice shortcut to ensure that a key exists. 
# Here is a short program that counts the number of occurrences of each letter in a string. 
# Open the file editor window and enter the following code, saving it as characterCount.py:

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# If you import the pprint module into your programs, 
# you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. 
# This is helpful when you want a cleaner display of the items in a dictionary than what print() provides.

# The program loops over each character in the message variable’s string, counting how often each character appears. 
# The setdefault() method call ➊ ensures that the key is in the count dictionary (with a default value of 0) 
# so the program doesn’t throw a KeyError error when count[character] = count[character] + 1 is executed ➋. 

# From the output, you can see that the lowercase letter c appears 3 times, 
# the space character appears 13 times, and the uppercase letter A appears 1 time. 
# This program will work no matter what string is inside the message variable, 
# even if the string is millions of characters long!