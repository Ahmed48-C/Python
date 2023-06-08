#This is a bot that plays the game Switch in crazygames.com 'https://www.crazygames.com/game/switch' it plays until score 20ish until the green obstacles appear then it dies because it a stupid bot):

import pyautogui
import time
import keyboard
import random
import win32api, win32con

#sleeps for 3 seconds so it gives time for the user to start the game
time.sleep(3)

#This is the click functions
def click(x,y):
    win32api.SetCursorPos((x,y)) #Here it specify where should the cursor be when the code below runs
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # this holds the left click in the mouse
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) # this release the left click in the mouse
    


# obstacles Y:  431

# this while loops runs until the user presses q    
while keyboard.is_pressed('q') == False:
    #left side
    #X:  413 Y:  515 RGB: (  0,   0,   0)
    if  pyautogui.pixel(416, 431)[0] == 0 and pyautogui.pixel(413, 515)[0] == 0: # this if statement first checks if the obstacle is in a specific pixel in the left side and the ball is on the left side 
        click(597, 515) # if so then this click function runs
        print("detected left side")
    #right side
    #X:  597 Y:  515 RGB: (  0,   0,   0)
    if   pyautogui.pixel(594, 431)[0] == 0 and pyautogui.pixel(597, 515)[0] == 0: # this if statement first checks if the obstacle is in a specific pixel in the right side and the ball is on the right side
        click(597, 515) # if so then this click function runs
        print("detected right side")




# while keyboard.is_pressed('q') == False:
#     #left side
#     #X:  413 Y:  515 RGB: (  0,   0,   0)
#     while  pyautogui.pixel(416, 431)[0] == 0 and pyautogui.pixel(413, 515)[0] == 0:
#         click(597, 515)
#         print("detected left side")
#         break
#     #right side
#     #X:  597 Y:  515 RGB: (  0,   0,   0)
#     while   pyautogui.pixel(594, 431)[0] == 0 and pyautogui.pixel(597, 515)[0] == 0: 
#         click(597, 515)
#         print("detected right side")
#         break