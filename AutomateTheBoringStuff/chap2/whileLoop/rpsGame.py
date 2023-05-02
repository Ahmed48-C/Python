# This is a Rock Paper Scissors Game

import random, sys, inquirer

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

rps = ["Rock", "Paper", "Scissors", "orQuit"]

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        questions = [
        inquirer.List('rpsChoices',
                    message="Choose your Move",
                    choices=rps,
                    ),
        ]
        choice = inquirer.prompt(questions)
        userChoice = choice['rpsChoices']
        if userChoice == 'orQuit':
            sys.exit() # Quit the program.
        if userChoice == 'Rock' or userChoice == 'Paper' or userChoice == 'Scissors':
            break # Break out of the player input loop.
        # print('Type one of r, p, s, or q.')
        print(userChoice)

    # Display what the player chose:
    if userChoice == 'Rock':
        print('ROCK versus...')
    elif userChoice == 'Paper':
        print('PAPER versus...')
    elif userChoice == 'Scissors':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'Rock'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'Paper'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'Scissors'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if userChoice == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif userChoice == 'Rock' and computerMove == 'Scissors' or userChoice == 'Paper' and computerMove == 'Rock' or userChoice == 'Scissors' and computerMove == 'Paper':
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1