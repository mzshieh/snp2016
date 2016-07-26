## Lecture 7

###Introduction to Python

+   What Is (Imperative) Programming?
    +   A sequence of instructions
    +   [Scratch](https://scratch.mit.edu)
+   What Is Python?
    +   A programming language
        +   Python 2 or 3?
    +   The interpreter
    +   The best first language to learn (According to the textbook author)
        +   However, in this course we started from Scratch.
+   Programmers Don't Need to Know Much Math
    +   Most programming does not require math beyond basic arithmetic.
+   Programming Is a Creative Activity
+   Downloading and Installing Python
    +   [Official Website](https://www.python.org/)
    +   Download Python 3
    +   Optional task: install python to your own computer
        +   All computers in the classroom are ready for use. 
+   The Interactive Shell
    +   Run `python`
    +   Run IDLE
+   How to Find Help
    +   Search engine
    +   Stackoverflow
+   Asking Smart Programming Questions
    +   解釋你想要做甚麼，不只是說你做了甚麼。能幫你的人才知道你有沒有走錯路。
    +   明確的指出甚麼地方有問題。比如說一開始就出錯，或是做了甚麼才出錯。
    +   將完整的錯誤訊息以及程式碼貼出。
        +   利用 [pastebin](http://pastebin.com/) 或 [gist](http://gist.github.com/) 來貼
    +   描述一下你已經做過哪些嘗試。代表你已經花了點力氣研究到底是怎麼一回事。
        +   這是有點關鍵。
    +   列出使用的 Python 版本以及開發環境。
        +   Python 2 跟 Python 3 有相當差異，有很多套件可能因為平台而有所不同。
    +   如果是改完部分 code 之後才產生的問題，請明確描述改了甚麼。
    +   給出可以重現問題的情境，前提盡量清楚。

### Python Basics

+   Expression
+   ERRORS ARE OKAY!
+   Arithmetic operators
+   Precedence
+   (Some) Data types
    +   Integer
    +   Floating-point number
    +   String
        +   Addition? No, it's concatenation.
        +   Multiplication? No, it's replication.
+   Storing Values in Variables
    +   Assignment
    +   Variable name
+   Dissecting Your Program
    +   Comments
    +   `print()`
    +   `input()`
    +   `len()`
    +   `str()`
    +   `int()`
    +   `float()`

### `pyautogui`

+   The computers mainly receive inputs from human via the mouse and the keyboard.
    +   If your program controls the mouse and the keyboard, then it can do a lot of things (just like the human beings).

+   Installation
    +   `pip install pyautogui`
        +   You might have trouble to install this package on your own computer.
        +   Report the problem to the teaching assistants if you cannot handle it.

+   Mouse
    +   Get the size of the screen
        +   `width, height = pyautogui.size()`
    +   Get the position of the mouse
        +   `x, y = pyautogui.position()`
    +   The coordinate system
        +   Top-left: (1,1)
        +   Bottom-right: `pyautogui.size()`
    +   Move
        +   To: `pyautogui.moveTo(x, y, duration)`
            +   You may ignore `duration`
        +   Relative: `pyautogui.moveRel(x, y, duration)`
    +   Click
        +   `pyautogui.click(x, y)`
        +   `pyautogui.rightClick(x, y)`
        +   `pyautogui.doubleClick(x, y)`
    +   Drag
        +   To: `pyautogui.dragTo(x, y, duration)`
        +   Relative: `pyautogui.dragRel(x, y, duration)`
    +   Scroll
        +   `pyautogui.scroll(y)`

+   Keyboard
    +   Type
        +   `pyautogui.typewrite(text,delay)`
    +   Press
        +   `pyautogui.press(key)`
        +   [Key table](https://automatetheboringstuff.com/chapter18/#calibre_link-36)
    +   Hot key
        +   `pyautogui.hotkey(key1, key2, ..., keys)`
        +   Example: `pyautogui.hotkey('ctrl', 'c')`

### Task 1

+   Draw a triangle
    +   Green
    +   Filled
+   Draw a rectangle
    +   Brown
    +   Filled
+   Draw a christmass tree
    +   [Example](https://scratch.mit.edu/projects/115904117/)

### Task 2

+   Draw a circle
    +   Green
    +   Filled
+   Draw a tilt rectangle
    +   Brown
    +   Filled
+   Draw a tree
    +   [With branches](https://scratch.mit.edu/projects/115838437)

### Task 3

+   Do whatever you want via using `pyautogui`