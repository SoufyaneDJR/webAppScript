import time
import pyautogui
import keyboard

buyMinCount = 0
playerNum = 0
activate = True

print('Running')

while True:

    if activate:
        if keyboard.is_pressed('UP'):
            pyautogui.click(x=982, y=882)  # Add 50
            pyautogui.click(x=1360, y=980)  # Search
            buyMinCount += 1

        if keyboard.is_pressed('RIGHT'):
            pyautogui.click(x=1500, y=715)  # Buy
            pyautogui.click(x=960, y=600)  # Confirm

        if keyboard.is_pressed('LEFT'):
            pyautogui.click(x=150, y=90)  # return to menu
            playerNum = 0

        if keyboard.is_pressed('DOWN'):
            pyautogui.click(x=454, y=882, clicks=buyMinCount, interval=0.1)  # return buy min to zero
            buyMinCount = 0

        if keyboard.is_pressed('space'):
            y = 408 + playerNum*140  # 140px distance beteen to player section in the trasnfer list
            pyautogui.click(x=825, y=y)  # Second player in the list
            playerNum += 1

    if keyboard.is_pressed('ctrl+space'):  # Activate or Deactivate Script
        activate = not activate
        print(activate)
        time.sleep(0.2)
