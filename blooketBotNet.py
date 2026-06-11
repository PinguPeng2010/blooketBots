from pynput.keyboard import Controller, Key
import pyautogui
import webbrowser
import time
import mss
import random





botNumber = int(input("Enter the number of bots: "))

botName = input("Enter the name of the bots: ")

botNameStartNumber = input("Enter the starting number for the bots: ")
code = (input("Enter the code: "))

# Opens bots
for x in range(0,botNumber):
    webbrowser.open_new_tab("https://play.blooket.com/play")

    print(f'Spawned {x+1} blooket bots')

time.sleep(1)

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

    pyautogui.typewrite(botName+ str(x) , interval=0)
    pyautogui.press('enter')
    print(f'{botName +str(x)} initialized')

    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

# Now it just clicks stuff

# First, inactive tabs (bots that haven't connected) are closed by checking the rgb value of a pixel.


def detectPixel(x, y):
    with mss.MSS() as sct:
        region = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(region)
        return img.pixel(0, 0)  # (R, G, B)

# On gold quest, blooket starts after 16 seconds


# On blooket, the background changes to a solid purple when connected. 111, 165 is the coord used.

culled = 0

for bot in range(0, botNumber):
    pixelColour = detectPixel(111, 165)
    print(f'Bot {botName +str(bot+int(botNameStartNumber))} pixel colour is {pixelColour}')


    if  pixelColour != (154, 73, 170):    # If the pixel is not purple, the bot is inactive, so we close it.

        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')

        culled += 1
        print(f'Bot {botName +str(bot+int(botNameStartNumber))} was culled')

    else:

        with keyboard.pressed(Key.ctrl):    # If it is the right colour move to next tab.
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            print(f'Bot {botName +str(bot+int(botNameStartNumber))} is safe')
    time.sleep(0.1)


print(f'{culled} bots culled')


# The script now asks if the user wants to autoc answer questions.

wantAutoAnswer = input("Do you want to auto answer questions? (y/n): ")

# TODO: Auto answer the questions using random
# TODO: Use mss to detect if the background is green to click.
# TODO: Use pyautogui to click boxes randomly for the bots.
# TODO: Use mss to detect if a swap or steal is selected, and use pyautogui to auto click the top right corner one.
# TODO: detect if the game is finshed using mss and auto ending the script.

