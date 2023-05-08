# Though dictionaries are not ordered, 
# the fact that you can have arbitrary values for the keys allows you to organize 
# your data in powerful ways. Say you wanted your program to store data about your friends’ birthdays.
# You can use a dictionary with the names as keys and the birthdays as values. 
# Open a new file editor window and enter the following code. Save it as birthdays.py.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("Enter a name:  (blank to quit)")
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')