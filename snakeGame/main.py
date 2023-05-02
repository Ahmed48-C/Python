from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS #setting the snake size to the body parts
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0]) # coordinates sets to 0x and 0y so that the snake appears in top left

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake") # creating the squares of the snake
            self.squares.append(square) # appending the square to the snake

class Food:
    
    def __init__(self):
        
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE # getting a random width from 14 different possibilities
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE # getting a random height from 14 different possibilities
    
        self.coordinates = [x,y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food") # creating an oval(food) and placing it in the random width and height we got above

def next_turn(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y)) #updating the snake coordinates

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR) #creating the squares of the snake

    snake.squares.insert(0, square) #inserting the new square to the snake

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        global SPEED

        score += 1

        if SPEED != 50:
            SPEED -= 10

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    #deleting the last square of the snake so it appears its moving
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False

def game_over():

    global game_ended

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 - 100, font=('consolas',30), text="Press Enter to restart", fill="white", tag="restart")
    game_ended = False

def start_new_game(event):

    global snake, food, direction, score, game_ended
    if not game_ended:
        game_ended = True
        canvas.delete("gameover", "restart")
        snake = Snake()
        food = Food()
        direction = 'down'
        score = 0
        label.config(text="Score:{}".format(score))
        next_turn(snake, food)

window = Tk()
window.title("Snake game")
window.resizable(False, False) # the game is not resizable

score = 0
direction = 'down'

game_ended = False

label = Label(window, text="Score:{}".format(score), font=('consoles', 40)) # making the score
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH) # making the canvas
canvas.pack()

window.update()

window_width = window.winfo_width() # width of the window
window_height = window.winfo_height() # height of the window
screen_width = window.winfo_screenwidth() # width of your screen
screen_height = window.winfo_screenheight() # height of your screen

# finding the difference between the center and the window
x = int((screen_width/2) - (window_width/2)) 
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}") #centering the window in the middle of the screen when it loads

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Return>', start_new_game)

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()