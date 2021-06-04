import pyautogui
import time
time.sleep(9)
beemovie = open("beemovie.txt", 'r')
for word in beemovie:
    time.sleep(0.4)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    print(word)




