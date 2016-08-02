## Lecture 9

### Review

+   Package installation is the hardest part in this course
    +   [Tutorial](../install.md)
+   Wait is important
    +   You have to wait until the precondition of the next instruction is established.
    +   Precondition and initialization
        +   Instant noodle
            +   What if you didn't boil the water?
        +   Scramble eggs
            +   What if you didn't scramble?
        +   Even experienced programmer may forget to initialize!
            +   The instructor forgot to fill hot water into the instant noodle cup.
+   `int()` will convert a `float` into integer
    +   Preserve the integral part only
        +   `int(1.9)` is `1`
        +   `int(0.5)` is `0`
        +   `int(-0.9)` is `0`
        +   `int(-1.7)` is `-1`
+   Formatting `float` 
    +   With string operator `%`: [`printf` style](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
        +   `%.3f` means print `3` digits after the decimal point.
    +   [New method](https://docs.python.org/3/library/stdtypes.html#str.format) is complicated. Not NOW.
+   For more information about the floating-point numbers in Python, please refer to the [official tutorial](https://docs.python.org/3/tutorial/floatingpoint.html).
    +   See also: [Wikipedia](https://en.wikipedia.org/wiki/IEEE_floating_point)
    +   Keyword: Binary numbers
+   Let's review the practice questions of [chapter 1](https://automatetheboringstuff.com/chapter1/).
+   `eval()` is powerful
+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
+   Comparison operators
    +   `==`
        +   `float` is not accurate.
        +   `float` can be `NaN` (not a number)
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

### Boolean values (Continued)

+   Truthy and falsey values
+   Truthy values
    +   Non-zero integers
    +   Non-zero `float`
    +   Non-empty `string`
+   Falsey values
    +   `0`
    +   `0.0`
    +   `''`
+   The are more truthy and falsey values. Not NOW.

### Flow Control: Selection

+   Conditions: a boolean expression
+   Block of code
    +   Don't forget colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
+   `if`
+   `else`
+   `elif`

### Task 1

`int()` is not ideal to convert `float` into `int`. Write a program that round a `float` into its closest integer.
+   Use `input()` and `print()`
+   You may assume the input is always a valid `float`
+   If there are two closest integers, then output the even one.
    +   四捨、六入、五成雙

### Flow Control: Loops

+   `while`
    +   `ctrl`+`C` to stop your (buggy) program
+   `break`
+   `continue`
+   `for`
+   `range()`
    +   `range(n)`: `0`, `1`, ..., `n-1`
    +   `range(start,stop)`: `start`, `start+1`, ..., `stop-1`
        +   Math: `[start,stop)`
    +   `range(start,stop,step)`: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step < stop`.
+   Nested loops

### Task 2

+   Draw a circle
    +   Green
    +   Filled
+   Draw a tilt rectangle
    +   Brown
    +   Filled
+   Draw a tree
    +   [With branches](https://scratch.mit.edu/projects/117415708/)

### Task 3

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)

### Practice Question: Chapter 2

+   See the [textbook](https://automatetheboringstuff.com/chapter2/)

### Flow Control: Exception

+   It is complicated. We are not going to cover much about it.
    +   Official [tutorial](https://docs.python.org/3/tutorial/errors.html)
+   [Example code](lec09-2.py)

### `import`

+   `sys`
    +   `sys.exit()`
+   `random`
    +   `random.random()`
    +   `random.randint()`
+   `pyperclip`
    +   `pyperclip.copy(str)`
    +   `pyperclip.paste()`