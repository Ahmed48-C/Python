import time, random
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import keyboard

TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        sleep_time = random.uniform(0.005, 0.009)
        time.sleep(sleep_time)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

while keyboard.is_pressed('q') == False:
    click_thread = threading.Thread(target=clicker)
    click_thread.start()


    with Listener(on_press=toggle_event) as listener:
        listener.join()