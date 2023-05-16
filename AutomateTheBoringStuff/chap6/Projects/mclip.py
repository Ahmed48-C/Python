# You want to be able to run this program with a command line argument that is a short key phrase—for instance, agree or busy. 
# The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email. 
# This way, the user can have long, detailed messages without having to retype them.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    value = input("Enter the value for the new keyphrase '{0}': ".format(keyphrase))
    TEXT[keyphrase] = value
    print('New key-value pair added to TEXT dictionary.')
    pyperclip.copy(value)
    print('Text for ' + keyphrase + ' copied to clipboard.')
