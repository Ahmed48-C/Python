# A Tic-Tac-Toe Board
# A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank. 
# To represent the board with a dictionary, you can assign each slot a string-value key

# You can use string values to represent what’s in each slot on the board: 'X', 'O', or ' ' (a space). 
# Thus, you’ll need to store nine strings. You can use a dictionary of values for this. 
# The string value with the key 'top-R' can represent the top-right corner, 
# the string value with the key 'low-L' can represent the bottom-left corner, 
# the string value with the key 'mid-M' can represent the middle, and so on.

# This dictionary is a data structure that represents a tic-tac-toe board. 
# Store this board-as-a-dictionary in a variable named theBoard. Open a new file editor window, 
# and enter the following source code, saving it as ticTacToe.py:
'''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

Since the value for every key in theBoard is a single-space string, 
this dictionary represents a completely clear board. If player X went first and chose the middle space, 
you could represent that board with this dictionary:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

A board where player O has won by placing Os across the top might look like this:

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

Of course, the player sees only what is printed to the screen, 
not the contents of variables. Let’s create a function to print the board dictionary onto the screen. 
Make the following addition to ticTacToe.py (new code is in bold):
'''

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)

# You can view the execution of this program at https://autbor.com/tictactoe1/. When you run this program, 
# printBoard() will print out a blank tic-tac-toe board.

#  | |
# -+-+-
#  | |
# -+-+-
#  | |

# The printBoard() function can handle any tic-tac-toe data structure you pass it. Try changing the code to the following:

# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)

# You can view the execution of this program at https://autbor.com/tictactoe2/. 
# Now when you run this program, the new board will be printed to the screen.

# O|O|O
# -+-+-
# X|X|  
# -+-+-
#  | |X

# Because you created a data structure to represent a tic-tac-toe board and wrote code in printBoard() to interpret that data structure, 
# you now have a program that “models” the tic-tac-toe board. 
# You could have organized your data structure differently (for example, using keys like 'TOP-LEFT' instead of 'top-L'), 
# but as long as the code works with your data structures, you will have a correctly working program.

# For example, the printBoard() function expects the tic-tac-toe data structure to be a dictionary with keys for all nine slots. 
# If the dictionary you passed was missing, say, the 'mid-L' key, your program would no longer work.

# O|O|O
# -+-+-
# Traceback (most recent call last):
#   File "ticTacToe.py", line 10, in <module>
#     printBoard(theBoard)
#   File "ticTacToe.py", line 6, in printBoard
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
# KeyError: 'mid-L'

# Now let’s add code that allows the players to enter their moves. Modify the ticTacToe.py program to look like this:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
            turn = 'O'
    else:
        turn = 'X'
    printBoard(theBoard)

# You can view the execution of this program at https://autbor.com/tictactoe3/. 
# The new code prints out the board at the start of each new turn ➊, gets the active player’s move ➋, 
# updates the game board accordingly ➌, and then swaps the active player ➍ before moving on to the next turn.