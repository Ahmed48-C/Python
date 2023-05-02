#The Collatz Sequence
#Challenge: Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. 
# (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. 
# Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
#Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

# Input Validation
# Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, 
# the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, 
# print a message to the user saying they must enter an integer.

#Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
import time

print("""\nHello This is the collatz sequence it will turn any number to 1 by dividing it by 2 and multiply it by 3 and then adding one. 
It will repeat this sequence as much times as it needs to finally make it 1 """)

def collatz(number):
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1

def numToOne():
    global userNumber
    
    try:
        userNumber = int(input("Enter a Number to turn it into 1: "))
        print("Collatz will turn {} into 1...".format(userNumber))
        
    except ValueError:
        print("\nOnly digits are allowed!\n")
        userNumber = int(input("Enter a Number to turn it into 1: "))
    print(userNumber)
    while True:
        if userNumber != 1: 
            print(collatz(userNumber))
            time.sleep(0.1)
            userNumber = collatz(userNumber)
            continue
        elif userNumber == 1:
            print("Thanks for playing!")
            break
              
numToOne()

        