#! python3
# 2048.py - This program plays the game at https://play2048.co/ automatically by
# repeatedly pressing the UP, RIGHT, DOWN, and LEFT arrow buttons. The user can
# quit the program at any time by pressing Ctrl+C.

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys

def play_2048():
    # Enter keystrokes repeatedly (up, right, down, left)
    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)

print('Welcome to the 2048 bot!')
print('Press Ctrl+C at any time to quit.')

# Open the browser to the game
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
while True:
    try:
        play_2048()
    # Exit the program if the user presses Ctrl+C
    except KeyboardInterrupt:
        print('Interrupted')
        break
        sys.exit(0)
