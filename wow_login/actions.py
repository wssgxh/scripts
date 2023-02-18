import pyautogui
import random
from time import sleep
import win32gui
# import OpenCV
# img = pyautogui.screenshot()
# img.save('tmp/screenshot.png')
# rgb = img.getpixel((100, 500))
# print(rgb)
# match = pyautogui.pixelMatchesColor(500,500,(12,120,400))
# print(match)

import win32gui
import win32con
import pyautogui
pyautogui.PAUSE = 1

action_list = ['3','5', 'space']

def switch_to_wow():
    window_id = win32gui.FindWindow(None, '魔獸世界')
    win32gui.SetForegroundWindow(window_id)
    win32gui.ShowWindow(window_id, win32con.SW_SHOW)
    sleep(1)

def get_character_head(time=1):

    for _ in range(0,time):
        if pyautogui.locateOnScreen('reference/img.png', confidence=0.5):
            print('bird head detected')
            return True
        else:
            print('bird head not detected!!')
        sleep(3)
    return False


def action_jump():
    switch_to_wow()
    sleep(0.5)
    pyautogui.press('w')
    pyautogui.press('w')
    pyautogui.press('space')

def random_actions():
    switch_to_wow()
    if get_character_head():
        item = random.choice(action_list)
        pyautogui.press(random.choice(item))
        print(f'action: {item}')


if __name__ == '__main__':

    switch_to_wow()
    while True:
        sleep(2)
        action_jump()