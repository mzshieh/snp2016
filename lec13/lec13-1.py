import pyautogui, time

def report():
    pos = pyautogui.position()
    color = pyautogui.screenshot().getpixel(pos)
    print('Mouse position:',pos,'Color:',color)
    
while True:
    report()
    time.sleep(0.1)

