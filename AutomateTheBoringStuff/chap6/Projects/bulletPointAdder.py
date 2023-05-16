# The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line,
# and then paste this new text to the clipboard. For example, 
# if I copied the following text (for the Wikipedia article “List of Lists of Lists”) to the clipboard:

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
