while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# In the first while loop, we ask the user for their age and store their input in age. If age is a valid (decimal) value,
# we break out of this first while loop and move on to the second, which asks for a password. Otherwise, 
# we inform the user that they need to enter a number and again ask them to enter their age. In the second while loop, 
# we ask for a password, store the user’s input in password, and break out of the loop if the input was alpha­numeric. 
# If it wasn’t, we’re not satisfied, so we tell the user the password needs to be alphanumeric and again ask them to enter a password.

# You can view the execution of this program at https://autbor.com/validateinput/. Calling isdecimal() and isalnum() on variables, 
# we’re able to test whether the values stored in those variables are decimal or not, alphanumeric or not. Here, these tests help us reject the input forty two but accept 42, 
# and reject secr3t! but accept secr3t.