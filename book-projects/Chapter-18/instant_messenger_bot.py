# !/usr/bin/python3
# instant_messenger_bot.py - Sends a message to a specific group of friends
# using Facebook messenger. This assumes that the user is already logged into
# messenger.

import time
import pyautogui

FRIEND_NAMES = ['Firstname Lastname']
MESSAGE = "Hey! How's it going?"
SEARCH_BOX = (61, 275)
MESSAGE_BOX = (622, 1031)

for friend in FRIEND_NAMES:
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL + C <<<')
    time.sleep(5)
    print(f'Sending {friend} a message...')

    # Find search box and click.
    pyautogui.click(SEARCH_BOX[0], SEARCH_BOX[1])

    # Search for friend name and wait to load.
    pyautogui.typewrite(friend)
    time.sleep(3)

    # Go down once and press 'enter' to choose the name.
    pyautogui.typewrite(['down', 'enter'])

    # Select the message box.
    pyautogui.click(MESSAGE_BOX[0], MESSAGE_BOX[1])

    # Type message and send it.
    pyautogui.typewrite(MESSAGE)
    pyautogui.typewrite('enter')
    
print('Done.')
