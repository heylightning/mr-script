
"""
THE FOLLOWING MODEL NAME: MR-01
THIS MODEL IS FOR THE COMPLETE GRIND OF THE INDIAN SERVER.
Note: The model is valid to grind PC points.
Note: Other servers can be grinded by altering the grind points and sleep() method timestamp.
Note: The required 'tab' presses might be altered due to the changes made in the browser my Microsoft.
"""

import random
import pyautogui
import webbrowser
from time import sleep
from data import idList, passList

rString='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCBNM1234567890'
webbrowser.open('runninggravity.com'); sleep(3)
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite("".join(list(random.sample(list(rString), random.randrange(5, 10)))))
pyautogui.press('enter'); sleep(10)

for mLoopIteration in range(1): # SET THE NUMBER OF IDs TO GRIND HERE
    pyautogui.press('alt'); sleep(3); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('enter'); sleep(10)
    pyautogui.press('tab', presses=2); pyautogui.press('enter'); sleep(10)
    pyautogui.press('alt'); sleep(3); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
    pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('enter')
    sleep(3); pyautogui.press('tab'); pyautogui.press('enter'); sleep(5)
    pyautogui.typewrite(idList[mLoopIteration]); pyautogui.press('enter')
    sleep(2); pyautogui.typewrite(passList[mLoopIteration]); pyautogui.press('enter')
    sleep(5); pyautogui.hotkey('shift', 'tab'); pyautogui.press('enter'); sleep(15)

    for dash_Points in range(1): # SET THE DASHBOARD GRIND POINT INTEGER HERE
        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite("".join(list(random.sample(list(rString), random.randrange(5, 10)))))
        pyautogui.press('enter'); sleep(10); pyautogui.press('alt'); sleep(3)
        pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
        pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
        pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
        pyautogui.press('tab'); pyautogui.press('enter'); sleep(5)
        pyautogui.press('tab', presses=4); pyautogui.press('enter'); sleep(3)
        pyautogui.hotkey('ctrl', 'w')  

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("".join(list(random.sample(list(rString), random.randrange(5, 10)))))
    pyautogui.press('enter'); sleep(3); pyautogui.press('f5'); sleep(5)

    for pc_g in range(3): # SET THE PC GRIND POINT INTEGER HERE
        pyautogui.press('alt'); sleep(3); pyautogui.press('tab')
        pyautogui.press('tab'); pyautogui.press('tab'); pyautogui.press('tab')
        pyautogui.press('tab'); pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite("".join(list(random.sample(list(rString), random.randrange(5, 10)))))
        pyautogui.press('enter'); sleep(3); 
    
    pyautogui.press('f5'); sleep(5); pyautogui.hotkey('ctrl', 'shift', 'i')
    sleep(2); pyautogui.press('alt'); sleep(3); pyautogui.press('tab', presses=3)
    pyautogui.press('enter'); pyautogui.press('f5'); sleep(10); pyautogui.hotkey('ctrl', 'l')
    sleep(3); pyautogui.press('tab', presses=20); sleep(3); pyautogui.press('tab', presses=2)
    pyautogui.hotkey('ctrl', 'a'); sleep(2); pyautogui.press('backspace')
    pyautogui.typewrite("".join(list(random.sample(list(rString), random.randrange(5, 10)))))
    pyautogui.press('enter'); sleep(3)
print('\nGrinding sucessfull.\n')

"""
Hint: MODEL NAME: MR-02
About: THIS IS TIME COMPLEX MODEL, THIS MODEL IS 300x TIMES THAN MR-01 IN TERMS OF BEING ROBUST AND FASTER.
    THIS MODEL CAN GRIND ON MULITPLE SERVERS WITH VPN AND CAN GRIND POINTS OF BOTH PC AND MOBILE.

OPEN SOURCING THE PROJECT SOON!
"""