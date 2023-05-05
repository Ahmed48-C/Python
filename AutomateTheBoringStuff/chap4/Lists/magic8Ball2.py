# Example Program: Magic 8 Ball with a List
# Using lists, you can write a much more elegant version of the previous chapter’s Magic 8 Ball program.
# Instead of several lines of nearly identical elif statements, 
# you can create a single list that the code works with. 
# Open a new file editor window and enter the following code. 
# Save it as magic8Ball2.py.

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

# When you run this program, 
# you’ll see that it works the same as the previous magic8Ball.py program.

# Notice the expression you use as the index for messages: 
# random.randint (0, len(messages) - 1). 
# This produces a random number to use for the index, 
# regardless of the size of messages. That is, you’ll get a random number between 0 and the value of len(messages) - 1. 
# The benefit of this approach is that you can easily add and remove strings to the messages list without changing other lines of code. 
# If you later update your code, there will be fewer lines you have to change and fewer chances for you to introduce bugs.