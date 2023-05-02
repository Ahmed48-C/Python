# Conditions will consider some values in other data types equivalent to True and False. 
# When used in conditions, 0, 0.0, and '' (the empty string) are considered False, 
# while all other values are considered True. For example, 
# look at the following program:

name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')