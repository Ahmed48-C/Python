import random, time
from inputimeout import inputimeout

numberOfQuestions = 10
correctAnswers = 0

difficulty = int(input('what is the range of numbers do you want'))

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, difficulty)
    num2 = random.randint(0, difficulty)
    
    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2) 
    
    questionAnswer = num1 * num2
    for i in range(3):
        try:
            answer = inputimeout(prompt, timeout=1000)
            answer = int(answer)
        except ValueError:
            print('Invalid input!')
            continue
        except Exception:
            print('Timeout')
            break
        
        if answer == questionAnswer:
            print('Correct!')
            correctAnswers += 1
            break
        else:
            print("Incorrect!") 
             
    time.sleep(0.5)      
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))