import re

passwordRegex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=\S+$).{8,}$')
password = input("Enter your password: ")
mo = passwordRegex.search(password)
if mo:
    print(mo.group() + "  is a strong password")
else:
    print("your password is weak!!")