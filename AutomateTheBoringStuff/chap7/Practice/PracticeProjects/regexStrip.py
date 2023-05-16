import re

test = "    hello world   "
space = re.compile(r'^\s+|\s+$')
print(space.sub('', test))

test2 = "aaaahello worldaaaa"
char = 'a'
char = re.compile('^[' + re.escape(char) + ']+|[' + re.escape(char) + ']+$')
print(char.sub('', test2))