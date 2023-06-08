import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    


# obstacles Y:  431
    
while keyboard.is_pressed('q') == False:
    #left side
    #X:  413 Y:  515 RGB: (  0,   0,   0)
    if pyautogui.pixel(413, 515)[0] == 0 and pyautogui.pixel(416, 431)[0] == 0:
        click(597, 515)
        print("detected left side")
    #right side
    #X:  597 Y:  515 RGB: (  0,   0,   0)
    if  pyautogui.pixel(597, 515)[0] == 0 and pyautogui.pixel(594, 431)[0] == 0:
        click(597, 515)
        print("detected right side")
