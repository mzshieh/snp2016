import pyautogui, time

pyautogui.FAILSAFE = True

loc = pyautogui.locateOnScreen('box.png')
while loc == None:
    time.sleep(0.1)
    loc = pyautogui.locateOnScreen('box.png')

for loc_i in pyautogui.locateAllOnScreen('box.png'):
    print(loc_i)
    center = pyautogui.center(loc_i)
    pyautogui.click(center)