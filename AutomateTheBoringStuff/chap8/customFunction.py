# Passing a Custom Validation Function to inputCustom()
# You can write a function to perform your own custom validation logic by passing the function to inputCustom(). For example, 
# say you want the user to enter a series of digits that adds up to 10. There is no pyinputplus.inputAddsUpToTen() function, 
# but you can create your own function that:

# Accepts a single string argument of what the user entered
# Raises an exception if the string fails validation
# Returns None (or has no return statement) if inputCustom() should return the string unchanged
# Returns a non-None value if inputCustom() should return a different string from the one the user entered
# Is passed as the first argument to inputCustom()
# For example, we can create our own addsUpToTen() function, and then pass it to inputCustom(). 
# Note that the function call looks like inputCustom(addsUpToTen) and not inputCustom(addsUpToTen()) because we are passing the addsUpToTen() 
# function itself to inputCustom(), not calling addsUpToTen() and passing its return value.

import pyinputplus as pyip
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers) # Return an int form of numbers.

response = pyip.inputCustom(addsUpToTen) # No parentheses after

# The inputCustom() function also supports the general PyInputPlus features, such as the blank, limit, timeout, default, allowRegexes,
# and blockRegexes keyword arguments. Writing your own custom validation function is useful when it’s otherwise difficult or 
# impossible to write a regular expression for valid input, as in the “adds up to 10” example.