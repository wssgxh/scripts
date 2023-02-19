import random
import win32gui
import win32con
import pyautogui

from time import sleep

pyautogui.PAUSE = 1

action_list = ['1', 'up', 'down', 'left', 'right', 'space']
len_action_list = len(action_list) - 1

def switch_to_wow():
    handle = win32gui.FindWindow(None, u'魔獸世界')
    win32gui.SetForegroundWindow(handle)

    # window_id = win32gui.FindWindow(None, '魔獸世界')
    # win32gui.SetForegroundWindow(window_id)
    # win32gui.ShowWindow(window_id, win32con.SW_SHOW)
    sleep(1)


def get_character_head(time=1):
    for _ in range(0, time):
        if pyautogui.locateOnScreen('reference/img.png', confidence=0.5):
            print('bird head detected')
            return True
        else:
            print('bird head not detected!!')
        sleep(3)
    return False


def is_queuing():
    switch_to_wow()
    if pyautogui.locateOnScreen('reference/queuing.png', confidence=0.5):
        return True
    else:
        return False


def is_enter_wow():
    switch_to_wow()
    if pyautogui.locateOnScreen('reference/enter_wow.jpg', confidence=0.5):
        print('enter_wow is ready ')
        return True
    else:
        return False

def minimize_window(name):
    def enumHandler(hwnd, lParam):
        if name in win32gui.GetWindowText(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    win32gui.EnumWindows(enumHandler, None)


def action_jump():
    switch_to_wow()
    sleep(0.5)
    pyautogui.press('w')
    pyautogui.press('w')
    pyautogui.press('space')


def random_actions():
    switch_to_wow()
    if get_character_head():
        index_key = random.randint(0, len_action_list)
        pyautogui.press(action_list[index_key])
        print(f'press {action_list[index_key]}')


if __name__ == '__main__':
    switch_to_wow()
    random_actions()