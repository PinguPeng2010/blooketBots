from pynput.keyboard import Controller, Key
import pyautogui
import webbrowser
import time
import mss

code = (input("Enter the code: "))


# Opens bots
for x in range(0,75):
    webbrowser.open_new_tab("https://play.blooket.com/play")
    print(f'Opened {x} google tabs')

time.sleep(0.5)
keyboard = Controller()

# Switches to the first tab
with keyboard.pressed(Key.ctrl):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

# For each bot enter code and switch to the next tab
for x in range(0,75):
    time.sleep(0.2) # Code is too fast, it caches the loading pages.
    pyautogui.typewrite(code, interval=0)
    pyautogui.press('enter')
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
time.sleep(0.2)
# Now type in nicknames for each bot
for x in range(0,75):
    time.sleep(0.2) # Same here, it is too fast, it caches the loading pages.
    pyautogui.typewrite('bot'+str(x), interval=0)
    pyautogui.press('enter')
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)


# Now it just clicks stuff
# Once game starts, random picks a number from 1-4, and pyautogui clicks it. It then moves to the next tab.
# After every bot has clicked, we go click, choose a number from one to 3, and click a position, and click again.
# Using mss, the bot will check if a pixel is red. If so

# First, inactive tabs (bots that haven't connected) are closed by checking the rgb value of a pixel.



