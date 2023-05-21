# PyInputPlus’s features can be useful for creating a timed multiplication quiz. By setting the allowRegexes, blockRegexes, timeout, 
# and limit keyword argument to pyip.inputStr(), you can leave most of the implementation to PyInputPlus. The less code you need to write, 
# the faster you can write your programs. Let’s create a program that poses 10 multiplication problems to the user, 
# where the valid input is the problem’s correct answer. Open a new file editor tab and save the file as multiplicationQuiz.py.

# First, we’ll import pyinputplus, random, and time. 
# We’ll keep track of how many questions the program asks and how many correct answers the user gives with the variables numberOfQuestions and 
# correctAnswers. A for loop will repeatedly pose a random multiplication problem 10 times:

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8, limit=3)  
    except pyip.TimeoutException:
        print('Out of time!')  
        
    except pyip.RetryLimitException:
        print('Out of tries!') 
        
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
        
    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))