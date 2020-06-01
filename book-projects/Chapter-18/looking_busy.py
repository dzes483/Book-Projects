#!/usr/bin/python3
# looking_busy.py - Nudges the mouse every ten seconds to prevent the display
# of an idle status in messaging programs.

import pyautogui
import time
import sys

print('Looking busy! Press Ctrl + C at any time to quit.')
while True:
    try:
        time.sleep(10)
        pyautogui.moveRel(10, 0, duration=0.25)
        time.sleep(10)
        pyautogui.moveRel(0, 10, duration=0.25)
        time.sleep(10)
        pyautogui.moveRel(-10, 0, duration=0.25)
        time.sleep(10)
        pyautogui.moveRel(0, -10, duration=0.25)
        time.sleep(10)
    except KeyboardInterrupt:
        sys.exit()
