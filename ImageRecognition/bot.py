import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(370, 350)[0] == 0:
        click(370, 350)
        
    if pyautogui.pixel(455, 350)[0] == 0:
        click(455, 350)
        
    if pyautogui.pixel(540, 350)[0] == 0:
        click(540, 350)
        
    if pyautogui.pixel(625, 350)[0] == 0:
        click(625, 350)

        
