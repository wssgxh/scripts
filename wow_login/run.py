import wmi
import win32com.client
import psutil
import time
import subprocess
import random
import pyautogui
import win32con
import pyautogui
import win32gui

from time import sleep
from actions import *
p


def close_programs_by_pid(pid_list, ignore):
    wmi = win32com.client.GetObject("winmgmts:")
    for pid in pid_list:

        if pid == ignore:
            continue
        process = wmi.ExecQuery("SELECT * FROM Win32_Process WHERE ProcessId = %d" % pid)[0]
        try:
            process.Terminate()
        except TypeError:
            pass


def get_process_running_time(pid):
    try:
        process = psutil.Process(pid)
        start_time = process.create_time()
        running_time = time.time() - start_time
        return running_time
    except psutil.NoSuchProcess:
        return None


def close_other_wow(wow_process_id):
    if len(wow_process_id) > 1:
        pid_ignore = 0
        shortest_time = 9999999
        for item in wow_process_id:
            tmp = get_process_running_time(item)
            if tmp < shortest_time:
                shortest_time = tmp
                pid_ignore = item
        close_programs_by_pid(wow_process_id, ignore=pid_ignore)


def run_wow():
    print('run a wow')
    cmd = '"C:\\Program Files (x86)\\Battle.net\\Battle.net.exe" --exec="launch WoWC"'
    subprocess.run(cmd, shell=True)


def get_wow_id():
    f = wmi.WMI()

    # Printing the header for the later columns
    wow_process_id = []
    wow_name = 'WowClassic.exe'

    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        if wow_name in process.Name:
            wow_process_id.append(process.ProcessId)

    return wow_process_id


if __name__ == "__main__":

    retry = 3
    counter = 0
    # init a wow instance
    while True:
        if len(get_wow_id()) == 0:
            print('wow not started, try again')
            run_wow()
            sleep(10)
            counter += 1
        else:
            print('wow started')
            break

        if counter > retry:
            exit(1)

    # run an another wow instance
    while True:
        if not get_character_head():
            print('bird head is not ready, will restart a wow')
            run_wow()
            sleep(10)
            pyautogui.getWindowsWithTitle("Battle.net")[0].minimize()
            close_other_wow(get_wow_id())
            sleep(20)
            switch_to_wow()
            sleep(0.5)
            pyautogui.press('enter')
            if get_character_head(10):
                random_actions()

        else:
            random_actions()
            sleep(random.uniform(1, 10))

