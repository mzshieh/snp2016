## Lecture 7

###Introduction to Python

+   What Is Programming?
+   What Is Python?
+   Programmers Don't Need to Know Much Math
+   Programming Is a Creative Activity
+   Downloading and Installing Python
+   The Interactive Shell
+   How to Find Help
+   Asking Smart Programming Questions

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
        +   `pyautogui.typewrite(text)`
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