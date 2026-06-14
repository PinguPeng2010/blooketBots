# blooketBotNet

`blooketBotNet.py` is a small Python automation script that opens multiple browser tabs and uses keyboard and screen input to interact with a Blooket session.

## Overview

- The script is built around timed browser automation and pixel checks. 
- It prompts for the number of bots, a name prefix, a starting number, and a game code.
- The bot then attempts to connect
- The script then will cull bots if they have not connected of if they have panicked.

## Requirements

The script depends on Python and the following packages:

- `pyautogui`
- `pynput`
- `mss`
- `pyperclip`

- An implementation to auto install the scripts will happen.

## Reliability

This program is only about 60% effective. Its success depends on website loading times, so results can vary between runs and even between individual tabs.

## Repository Notes

- The main script is [blooketBotNet.py](blooketBotNet.py).

## Caution

- Not my fault if u get banned lol
- Maybe use without your account on