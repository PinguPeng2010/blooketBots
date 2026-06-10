import webbrowser
import time
from pynput.keyboard import Controller, Key

keyboard = Controller()

time.sleep(3)
code = 1880618
url = "https://play.blooket.com/play"
x = 1
name = 'rahulbot'


while x!= 50:
    webbrowser.open_new_tab(url)
    time.sleep(0.6)
    keyboard.type(str(code))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.type(name+str(x))
    x+=1
    print(f'Opened {x} google tabs')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)



