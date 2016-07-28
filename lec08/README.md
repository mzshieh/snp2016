## Lecture 8

### Review

+   Goal:
    +   To teach imperative programming
        +   Functions
        +   Syntax
        +   Algorithms
    +   To teach how to control computers
+   Approach: limited but sufficient information
    +   Might be against the best practice
        +   You may learn more after this course
+   The Interactive Shell
    +   Run `python`
    +   Run IDLE
+   How to Find Help
    +   Search engine
    +   [Stackoverflow](http://stackoverflow.com/)
    +   Asking Smart Programming Questions
+   Expression
    +   Values and operators
    +   Arithmetic operators: `+` `-` `*`, `/`, `//`, `%`, `**`, `()`
+   Data types
    +   Integer: exact
    +   Floating-point number: accurate enough in practice
    +   String
        +   Concatenate: `+`
        +   Repeat: `*`

### `pyautogui`

+   First: `import pyautogui`
+   Then, turn off `FAILSAFE`: `pyautogui.FAILSAFE = False`
+   Mouse
    +   Get the size of the screen
        +   `width, height = pyautogui.size()`
    +   Get the position of the mouse
        +   `x, y = pyautogui.position()`
    +   The coordinate system
        +   Top-left: (0,0)
        +   Bottom-right: `pyautogui.size()`-(1,1)
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

+   For those who feel `pyautogui` is too long, please try `gui = pyautogui` then `gui.moveTo(1,1)`
    +   This might make your code hard to read.

### Task 0

+   Goal: Open Microsoft Paint and maximize it
+   Using mouse (with your eyes?)
    +   Click start
    +   Find the application and click it
    +   Wait until Microsoft Paint is opened (Important)
    +   Click the maximize button
+   Using keyboard (without your eyes?)
    +   Press windows key (Click start?)
    +   Type `mspaint` (Find the application?)
    +   Press enter (Click it?)
    +   Wait until Microsoft Paint is opened
    +   Hold windows key, then press up (Maximize)
+   [Sample code](lec08-1.py)
+   If the task is not a provided function, then you have to program.
+   Decompose the task into instructions supported by the system environment.

### Task 1

+   Task 1-1: Draw a triangle
    +   Green
    +   Filled
+   Task 1-2: Draw a rectangle
    +   Brown
    +   Filled
+   Task 1-3: Draw a christmass tree
    +   [Example](https://scratch.mit.edu/projects/115904117/)

+   Try to decompose task 1 into instructions
    +   Mouse actions: move, drag, click
    +   Keyboard actions: press, type, hotkey

### Python Basics (Continued)

+   Storing Values in Variables
    +   Assignment
    +   Variable name has some limitation
        +   See the [textbook](https://automatetheboringstuff.com/chapter1/#calibre_link-107)
+   Comments
    +   Starting with `#`
    +   Interpreter will ignore the comments

+   (Some) Functions
    +   A sequence of instructions
        +   A mini-program in a program
    +   `print()`
        +   Display the value between `(` and `)`
        +   Almost the only thing you can do in the first programming course.
    +   `input()`
        +   Read a string from the interactive shell.
    +   `len()`
        +   Calculate the length of a `string`
    +   `str()`
        +   Convert things into `string`
    +   `int()`
        +   Convert things into `int`
    +   `float()`
        +   Convert things into `float`
    +   `eval()`
        +   Try `eval(input())`

### Chapter 1

+   [Practice Questions](https://automatetheboringstuff.com/chapter1/)

### Flow Control

+   [Flow chart](https://automatetheboringstuff.com/chapter2/#calibre_link-1903)
+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
+   Comparison operators
    +   `==`
        +   `float` is not accurate.
    +   `!=`
    +   `<`
    +   `<=`
    +   `>`
    +   `>=`
    +   Compare values of different types
        +   `string` versus `int`
        +   `int` versus `float`
+   Boolean operators
    +   `and`
    +   `or`
    +   `not`
    +   Precedence: `not` > `and` > `or`

+   Conditions: a boolean expression
+   Block of code
+   `if`
+   `else`
+   `elif`
+   `while`
+   `break`
+   `continue`
+   `for`
+   `range()`

## Task 2

+   Draw a circle
    +   Green
    +   Filled
+   Draw a tilt rectangle
    +   Brown
    +   Filled
+   Draw a tree
    +   [With branches](https://scratch.mit.edu/projects/115838437)
