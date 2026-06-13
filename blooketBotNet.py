from pynput.keyboard import Controller, Key
import pyautogui
import webbrowser
import time
import mss
import random

bots = {}   # A dictionary to store the answer status of the bots. The value can either be 'question' or 'red' depending on if the bot is ready to answer a question or got the answer wrong.


botNumber = int(input("Enter the number of bots: "))
botName = input("Enter the name of the bots: ")
botNameStartNumber = input("Enter the starting number for the bots: ")
code = (input("Enter the code: "))


# JS cheats
allCorrect = 'javascript:(()=>{const c=async()=>{var e=Object.values(function e(t=document.querySelector("body>div")){return Object.values(t)[1]?.children?.[0]?._owner.stateNode?t:e(t.querySelector(":scope>div"))}())[1].children[0]._owner["stateNode"];e.freeQuestions=e.questions=e.props.client.questions.map(e=>({...e,correctAnswers:e.answers}))};let i=new Image;i.src="https://raw.githubusercontent.com/Coding4hours/Blooket-Cheats/main/autoupdate/timestamps/global/everyAnswerCorrect.png?"+Date.now(),i.crossOrigin="Anonymous",i.onload=function(){var e=document.createElement("canvas").getContext("2d");e.drawImage(i,0,0,this.width,this.height);let t=e.getImageData(0,0,this.width,this.height)["data"],r="",o;for(let e=0;e<t.length;e+=4){var n=String.fromCharCode(256*t[e+1]+t[e+2]);if(r+=n,"/"==n&&"*"==o)break;o=n}var e=document.querySelector("iframe"),[,a,s]=r.match(/LastUpdated: (.+?); ErrorMessage: "(.+?)"/);(parseInt(a)<=1693429947386||e.contentWindow.confirm(s))&&c()},i.onerror=i.onabort=()=>(i.src=null,c())})();'
allTriple = 'javascript:(()=>{const i=async()=>{let t=Object.values(function e(t=document.querySelector("body>div")){return Object.values(t)[1]?.children?.[0]?._owner.stateNode?t:e(t.querySelector(":scope>div"))}())[1].children[0]._owner["stateNode"];0==t.state.gold&&t.setState({gold:100,gold2:100}),t._choosePrize||=t.choosePrize,t.choosePrize=function(e){t.state.choices[e]={type:"multiply",val:3,text:"Triple Gold!",blook:"Unicorn"},t._choosePrize(e)}};let c=new Image;c.src="https://raw.githubusercontent.com/Coding4hours/Blooket-Cheats/main/autoupdate/timestamps/gold/alwaysTriple.png?"+Date.now(),c.crossOrigin="Anonymous",c.onload=function(){var e=document.createElement("canvas").getContext("2d");e.drawImage(c,0,0,this.width,this.height);let t=e.getImageData(0,0,this.width,this.height)["data"],o="",r;for(let e=0;e<t.length;e+=4){var a=String.fromCharCode(256*t[e+1]+t[e+2]);if(o+=a,"/"==a&&"*"==r)break;r=a}var e=document.querySelector("iframe"),[,n,s]=o.match(/LastUpdated: (.+?); ErrorMessage: "(.+?)"/);(parseInt(n)<=1693429947442||e.contentWindow.confirm(s))&&i()},c.onerror=c.onabort=()=>(c.src=null,i())})();'

# Opens bots
for x in range(0,botNumber):
    webbrowser.open_new_tab("https://play.blooket.com/play")

    print(f'Spawned {x+1} blooket bots')



time.sleep(1) # Waits for page to load.



keyboard = Controller() # For pynput




def nextTab():      # Goes to the next tab using ctrl + tab

    with keyboard.pressed(Key.ctrl):

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)



def detectPixel(x, y):      # Detects the RGB value of a pixel using mss.

    with mss.MSS() as sct:

        region = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(region)

        return img.pixel(0, 0)  # (R, G, B)



def pickAnswer(start, end):     # Chooses a random answer or box to click.
    
    return random.randint(start, end)



def screenType():   # Identifies the screen type using R G B values of screen picture.
    
    if detectPixel(930, 400) == (196, 58, 53): # Red
        return "red"
    
    elif detectPixel(930, 400) == (58, 196, 53): # Green
        return "green"
    
    elif detectPixel(700, 710) == (115, 57, 37): # Chest
        return "chest"
    
    elif detectPixel(50, 500) == (255, 255, 255): # Question
        return "question"

    elif detectPixel(800, 450) == (11, 194, 207): # loading 
        return "loading"
    
    elif detectPixel(1174, 485) == (255, 255, 255): # Finish 
        return "finish"



    else:
        raise Exception("Unknown screen type")
    
def getBotStatus(bot):
    global bots
    return bots[bot]

def changeBotStatus(bot, status):
    global bots
    try:
        bots[bot] = status
        return True
    except:
        raise Exception(f'Bot {bot} was unable to change status')

# For each bot enter code and switch to the next tab #

for x in range(0,botNumber):

    pyautogui.typewrite(code, interval=0)
    pyautogui.press('enter')

    nextTab()
    time.sleep(0.2)     # Code is too fast, it caches the loading pages.



# Now type in nicknames for each bot #

for x in range(int(botNameStartNumber),botNumber + int(botNameStartNumber)):


    pyautogui.typewrite(botName+ str(x) , interval=0)
    pyautogui.press('enter')
    print(f'{botName +str(x)} initialized')

    nextTab()
    time.sleep(0.2) # Same here, it is too fast, it caches the loading pages.



# Now bots can answer questions #


# First, inactive tabs (bots that haven't connected) are closed by checking the rgb value of a pixel.

culled = 0


for bot in range(0, botNumber):

    pixelColour = detectPixel(111, 165)

    print(f'Bot {botName +str(bot+int(botNameStartNumber))} pixel colour is {pixelColour}')


    if pixelColour == (255, 255, 255):    # If the pixel is white, the page hasn't loaded, so we wait and check again.
        
        time.sleep(0.2)
        if  pixelColour != (154, 73, 170):    # If the pixel is not purple, the bot is inactive, so we close it.
            
            with keyboard.pressed(Key.ctrl):

                keyboard.press('w')
                keyboard.release('w')

            culled += 1

            print(f'Bot {botName +str(bot+int(botNameStartNumber))} was culled')

        else:

            nextTab()    # If it is the right colour move to next tab.

            print(f'Bot {botName +str(bot+int(botNameStartNumber))} is safe')

    elif  pixelColour != (154, 73, 170):    # If the pixel is not purple, the bot is inactive, so we close it.

        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')

        culled += 1

        print(f'Bot {botName +str(bot+int(botNameStartNumber))} was culled')
    else:

        nextTab()    # If it is the right colour move to next tab.

        print(f'Bot {botName +str(bot+int(botNameStartNumber))} is safe')
        changeBotStatus(botName +str(bot+int(botNameStartNumber)), 'nocheat') # Adds the bot to dict to say it is ready to answer a question.
        print(f"Bot {botName +str(bot+int(botNameStartNumber))}'s status is {getBotStatus(botName + str(bot+int(botNameStartNumber)))}")


    time.sleep(0.2)


print(f'{culled} bots culled')
print(f'{botNumber - culled} bots remaining')

nextTab()


# TODO: Auto answer the questions using random
# TODO: Use mss to detect if the background is green to click. DONE
# TODO: Use pyautogui to click boxes randomly for the bots.
# TODO: Use mss to detect if a swap or steal is selected, and use pyautogui to auto click the top right corner one.
# TODO: detect if the game is finshed using mss and auto ending the script. 


# Every bot must now open ctrl+shift+j, paste in and close the console.

time.sleep(20)

for bot in bots:
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press('j')
            keyboard.release('j')
    
    pyautogui.typewrite(allCorrect, interval=0)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.typewrite(allTriple, interval=0)
    pyautogui.press('enter')
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press('j')
            keyboard.release('j')

    changeBotStatus(bot, 'cheatson')
    print(f"Bot {bot}'s status is {getBotStatus(bot)}")
    time.sleep(0.1)
    nextTab()

 




# This cheat makes every answer correct #







# finished = False


# while not finished:

#     # The bot first must identify if it is on an answer screen, a red screen, the loading screen, or the finish screen.

#     screen = screenType()

#     print(f"Bot {botName+str(botNameStartNumber+bot)}'s Screen type is {screen}")
    
#     if screen == 'loading':
#         continue
        


    # If the bot has answered correctly, it can now click a chest

        


