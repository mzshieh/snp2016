import pyautogui, random

pyautogui.FAILSAFE = False

x, y = pyautogui.position()
if x < 100:
    pyautogui.moveTo(10,y)

x, y = pyautogui.position()
if x < 100 and y > 100:
    pyautogui.moveTo(123, 456, 1)
else:
    pyautogui.moveTo(0,y)

x, y = pyautogui.position()
while not (x < 100 and y < 100):
    dx = random.randint(-10,10)
    dy = random.randint(-10,10)
    pyautogui.moveRel(dx, dy)
    pyautogui.moveRel(0,0,0.5)
    x, y = pyautogui.position()