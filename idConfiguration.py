import random
import pyautogui
import webbrowser
from time import sleep
from data import idList, passList

webbrowser.open('bloomreact.com'); sleep(3)
pyautogui.hotkey('ctrl', 'shift', 'n'); sleep(2)
bdMonth = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# Here the range is the number of IDs you want to make at a time.
for pro_IDs in range(2):
    pyautogui.typewrite('https://signup.live.com/signup'); pyautogui.press('enter'); sleep(30)
    pyautogui.typewrite(idList[pro_IDs])
    pyautogui.press('enter'); sleep(2)
    pyautogui.typewrite(passList[pro_IDs]); pyautogui.press('enter')
    sleep(2); tempList = idList[pro_IDs].split('.')
    pyautogui.typewrite(tempList[0]); pyautogui.press('tab')
    pyautogui.typewrite(tempList[1]); pyautogui.press('enter'); sleep(2)
    pyautogui.press('tab'); pyautogui.typewrite(random.choice(bdMonth))
    pyautogui.press('tab'); pyautogui.typewrite(str(random.randrange(1, 29)))
    pyautogui.press('tab')
    pyautogui.typewrite('2001'); pyautogui.press('enter'); sleep(60)
    pyautogui.hotkey('ctrl', 'w'); sleep(3); pyautogui.hotkey('ctrl', 'shift', 'n'); sleep(3)