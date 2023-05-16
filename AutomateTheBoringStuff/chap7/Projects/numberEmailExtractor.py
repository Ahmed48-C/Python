# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# What if you want to use re.VERBOSE to write comments in your regular expression but also want to use re.IGNORECASE to ignore capitalization? 
# Unfortunately, the re.compile() function takes only a single value as its second argument. 
# You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), 
# which in this context is known as the bitwise or operator.

# So if you want a regular expression that’s case-insensitive and includes newlines to match the dot character, 
# you would form your re.compile() call like this:

# >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

# Including all three options in the second argument will look like this:

# >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# This syntax is a little old-fashioned and originates from early versions of Python. The details of the bitwise operators are beyond the scope of this book, 
# but check out the resources at https://nostarch.com/automatestuff2/ for more information. You can also pass other options for the second argument; 
# they’re uncommon, but you can read more about them in the resources, too.

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.


import pyperclip, re

# Create phone number regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')