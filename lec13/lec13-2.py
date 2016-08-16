import pyautogui, time

pyautogui.FAILSAFE = True

stages = ['choose_tool.png','choose_color.png']
for stage in stages:
    loc = None
    while loc == None:
        loc = pyautogui.locateOnScreen(stage)
        time.sleep(0.1)
    center = pyautogui.center(loc)
    pyautogui.click(center)
