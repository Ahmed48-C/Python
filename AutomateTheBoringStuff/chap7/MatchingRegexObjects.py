# A Regex object’s search() method searches the string it is passed for any matches to the regex. 
# The search() method will return None if the regex pattern is not found in the string. If the pattern is found, 
# the search() method returns a Match object, which have a group() method that will return the actual matched text from the searched string. 
# (I’ll explain groups shortly.)
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


# The mo variable name is just a generic name to use for Match objects. This example might seem complicated at first, 
# but it is much shorter than the earlier isPhoneNumber.py program and does the same thing.

# Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex. Then we call search() on phoneNumRegex and pass search() 
# the string we want to match for during the search. The result of the search gets stored in the variable mo. In this example, we know that our pattern will be found in the string, 
# so we know that a Match object will be returned. Knowing that mo contains a Match object and not the null value None, 
# we can call group() on mo to return the match. Writing mo.group() 
# inside our print() function call displays the whole match, 415-555-4242.