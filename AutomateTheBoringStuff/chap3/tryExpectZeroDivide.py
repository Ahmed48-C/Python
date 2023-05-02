# Errors can be handled with try and except statements. The code that could potentially have an error is put in a try clause. 
# The program execution moves to the start of a following except clause if an error happens.

# You can put the previous divide-by-zero code in a try clause and have an except clause contain code to handle what happens 
# when this error occurs.

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
