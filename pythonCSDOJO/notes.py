# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""



# Also, use the global keyword if you want to change a global variable inside a function.
# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""



# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# Example
"""
a = "Hello World"	
#type is str	

b = 20	    
#type is int	

c = 20.5	
#type is float	

d = 1j	
#type is complex	

e = ["apple", "banana", "cherry"]	
#type is list	

f = ("apple", "banana", "cherry")	
#type is tuple	

g = range(6)	
#type is range	

h = {"name" : "John", "age" : 36}	
#type is dict	

i = {"apple", "banana", "cherry"}	
#type is set	

j = frozenset({"apple", "banana", "cherry"})	
#type is frozenset	

k = True	
#type is bool	

l = b"Hello"	
#type is bytes	

m = bytearray(5)	
#type is bytearray	

n = memoryview(bytes(5))	
#type is memoryview	

o = None	
#type is NoneType	
"""

# If you want to specify the data type 
# you can write the data type and () example: str()
# the data you want to specify its type should be inside the brackets

# Import the random module, and display a random number between 1 and 9:
"""
import random
print(random.randrange(1, 10))
"""



# Check String
# To check if a certain phrase or character is present in a string,
# we can use the keyword in.

# Example
# Print only if "free" is present:
"""
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
"""

# Check if NOT
# To check if a certain phrase or character is NOT present in a string,
# we can use the keyword not in.

# Example
# Check if "expensive" is NOT present in the following text:
"""
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
"""



# Upper Case
# Example
# The upper() method returns the string in upper case:
"""
a = "Hello, World!"
print(a.upper())
"""
# Lower Case
# Example
# The lower() method returns the string in lower case:
"""
a = "Hello, World!"
print(a.lower())
"""

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:
"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
"""

# Replace String
# Example
# The replace() method replaces a string with another string:
"""
a = "Hello, World!"
print(a.replace("H", "J"))
"""

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:
"""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
"""

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Example
# Use the format() method to insert numbers into strings:
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""

# Example
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
"""

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""



# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.
# Example
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
""" txt = "We are the so-called "Vikings" from the north." """

# To fix this problem, use the escape character \":
# Example
# The escape character allows you to use double quotes when you normally would not be allowed:
""" txt = "We are the so-called \"Vikings\" from the north." """

# Escape Characters
# Other escape characters used in Python:
"""
\'	#Single Quote	
\\	#Backslash	
\n	#New Line	
\r	#Carriage Return	
\t	#Tab	
\b	#Backspace	
\f	#Form Feed	
\ooo	#Octal value	
\xhh	#Hex value
"""



# String Methods
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.
"""
capitalize()	#Converts the first character to upper case
casefold()	#Converts string into lower case
center()	#Returns a centered string
count()	#Returns the number of times a specified value occurs in a string
encode()	#Returns an encoded version of the string
endswith()	#Returns true if the string ends with the specified value
expandtabs()	#Sets the tab size of the string
find()	#Searches the string for a specified value and returns the position of where it was found
format()	#Formats specified values in a string
format_map()	#Formats specified values in a string
index()	#Searches the string for a specified value and returns the position of where it was found
isalnum()	#Returns True if all characters in the string are alphanumeric
isalpha()	#Returns True if all characters in the string are in the alphabet
isdecimal()	#Returns True if all characters in the string are decimals
isdigit()	#Returns True if all characters in the string are digits
isidentifier()	#Returns True if the string is an identifier
islower()	#Returns True if all characters in the string are lower case
isnumeric()	#Returns True if all characters in the string are numeric
isprintable()	#Returns True if all characters in the string are printable
isspace()	#Returns True if all characters in the string are whitespaces
istitle()	#Returns True if the string follows the rules of a title
isupper()	#Returns True if all characters in the string are upper case
join()	#Joins the elements of an iterable to the end of the string
ljust()	#Returns a left justified version of the string
lower()	#Converts a string into lower case
lstrip()	#Returns a left trim version of the string
maketrans()	#Returns a translation table to be used in translations
partition()	#Returns a tuple where the string is parted into three parts
replace()	#Returns a string where a specified value is replaced with a specified value
rfind()	#Searches the string for a specified value and returns the last position of where it was found
rindex()	#Searches the string for a specified value and returns the last position of where it was found
rjust()	#Returns a right justified version of the string
rpartition()	#Returns a tuple where the string is parted into three parts
rsplit()	#Splits the string at the specified separator, and returns a list
rstrip()	#Returns a right trim version of the string
split()	#Splits the string at the specified separator, and returns a list
splitlines()	#Splits the string at line breaks and returns a list
startswith()	#Returns true if the string starts with the specified value
strip()	#Returns a trimmed version of the string
swapcase()	#Swaps cases, lower case becomes upper case and vice versa
title()	#Converts the first character of each word to upper case
translate()	#Returns a translated string
upper()	#Converts a string into upper case
zfill()	#Fills the string with a specified number of 0 values at the beginning
"""