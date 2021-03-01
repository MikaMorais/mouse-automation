
import pyautogui, sys
import time


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

timeout = time.time() + 60 * 1


try:    
        
    while time.time() < timeout:
        
        pyautogui.moveTo(250, 250, duration = 1)
        pyautogui.move(300, 0, duration = 1)
        pyautogui.move(0, 200, duration = 1)
        pyautogui.move(-200, 0, duration = 1)
        pyautogui.move(0, -200, duration = 1)

except KeyboardInterrupt:
    print('DONE')
