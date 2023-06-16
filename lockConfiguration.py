import pyautogui
import webbrowser 
import pyperclip
from time import sleep
from data import idList, passList

webbrowser.open('runninggravity.com'); sleep(2)
# Here range is the number of IDs you want to grind at a time.
for idIteration in range(10):
    pyautogui.hotkey('ctrl', 'shift', 'n'); sleep(3)
    pyautogui.typewrite('https://login.microsoftonline.com/')
    pyautogui.press('enter'); sleep(5); pyautogui.typewrite(idList[idIteration])
    pyautogui.press('enter'); sleep(5); pyautogui.typewrite(passList[idIteration])
    pyautogui.press('enter'); sleep(10); pyautogui.hotkey('ctrl', 'l'); 
    pyautogui.hotkey('ctrl', 'c'); compareString = pyperclip.paste(); 
    if(compareString[0 : 31] == 'https://account.live.com/Abuse?'):
        print(f'\nID {idIteration + 1}: ' + idList[idIteration] + ' is locked.\n')
    else:
        print(f'\nID {idIteration + 1}: ' +  idList[idIteration] + ' is fine.\n')
    pyautogui.hotkey('ctrl', 'w')
print('\nConfiguration Successfull.\n')