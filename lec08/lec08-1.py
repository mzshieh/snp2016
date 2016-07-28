#   載入套件
import pyautogui

#   關掉安全模式，避免程式在滑鼠滑到左上角時中斷。
pyautogui.FAILSAFE = False

#   按 Windows 鍵：按開始
pyautogui.press('win')

#   輸入 mspaint 後按 Enter 鍵，執行小畫家
pyautogui.typewrite('mspaint')
pyautogui.press('enter')

#   滑鼠跑到左上角，並浪費兩秒鐘。
#   重點是要浪費兩秒鐘等小畫家打開，不然接不上下一個動作。
pyautogui.moveTo(0,0,2)

#   同時按下 Windows 鍵與 上箭頭 鍵，用熱鍵將小畫家最大化。
pyautogui.hotkey('win','up')

#   多按幾下確保有最大化
pyautogui.hotkey('win','up')
pyautogui.hotkey('win','up')
pyautogui.hotkey('win','up')
