from pynput.keyboard import Controller, Key
import pyautogui
import webbrowser
import time
import mss
import random



code = (input("Enter the code: "))

botNumber = int(input("Enter the number of bots: "))

botName = input("Enter the name of the bots: ")

botNameStartNumber = input("Enter the starting number for the bots: ")

# Opens bots
for x in range(0,botNumber):
    webbrowser.open_new_tab("https://play.blooket.com/play")

    print(f'Opened {x} google tabs')

time.sleep(0.5)

keyboard = Controller() # For pynput

# Switches to the first tab
with keyboard.pressed(Key.ctrl):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

# For each bot enter code and switch to the next tab
for x in range(0,botNumber):

    time.sleep(0.2) # Code is too fast, it caches the loading pages.

    pyautogui.typewrite(code, interval=0)
    pyautogui.press('enter')

    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

# Now type in nicknames for each bot
for x in range(int(botNameStartNumber),botNumber + int(botNameStartNumber)):

    time.sleep(0.2) # Same here, it is too fast, it caches the loading pages.

    pyautogui.typewrite('bot'+ str(x) , interval=0)
    pyautogui.press('enter')


    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

time.sleep()
# Now it just clicks stuff
# Once game starts, random picks a number from 1-4, and pyautogui types it. It then moves to the next tab.
# After every bot has clicked, we go click, choose a number from one to 3, and click a position, and click again.
# Using mss, the bot will check if a pixel is red. If so

# First, inactive tabs (bots that haven't connected) are closed by checking the rgb value of a pixel.


def detectPixel(x, y):
    with mss.MSS() as sct:
        region = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(region)
        return img.pixel(0, 0)  # (R, G, B)

# On gold quest, blooket starts after 16 seconds


# On blooket, the background changes to a solid purple when connected. 111, 165 is the coord used.

for bot in range(0, botNumber):

    if detectPixel(111, 165) != (154, 73, 170):    # If the pixel is not purple, the bot is inactive, so we close it.

        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')

    else:

        with keyboard.pressed(Key.ctrl):    # If it is the right colour move to next tab.
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)



