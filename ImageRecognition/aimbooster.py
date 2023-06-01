import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(180,340,600,420))  
    
    width, height = pic.size      
    
    for x in range(0,width,5):
        for y in range(0,height,5):
            
            r,g,b = pic.getpixel((x,y))
            
            if b == 195:
                click(x+180,y+340)
                time.sleep(0.05)
                break
            
    
# 180,340,600,420
# iml = pyautogui.screenshot(region=(180,340,600,420))
# iml.save(r"C:\Users\Karim\Desktop\Python\ImageRecognition\savedimage.png")