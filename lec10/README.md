## Lecture 10

### Flow Control: Exception

+   It is complicated. We are not going to cover much about it.
    +   Official [tutorial](https://docs.python.org/3/tutorial/errors.html)
+   Syntax error
+   Exception
+   [Example code 1](lec10-1.py)
+   [Example code 2](lec10-2.py)
    +   Error type: printed on the shell

### `import`

+   `sys`
    +   `sys.exit()`
+   `random`
    +   `random.random()`
    +   `random.randint(L,U)`
        +   Inclusive, inclusive: [`L`,`U`]
    +   `random.randrange(n)`
    +   `random.randrange(start,stop)`
    +   `random.randrange(start,stop,step)`
+   `pyperclip`
    +   `pyperclip.copy(str)`
    +   `pyperclip.paste()`

### Review

+   Boolean Values
    +   `True`
    +   `False`
    +   `true` and `false` are no good
+   Boolean operatorssk
    +   `and`
    +   `or`
    +   `not`
    +   Precedence: `not` > `and` > `or`
+   Truthy and falsey values
    +   Truthy values
        +   Non-zero integers
        +   Non-zero `float`
        +   Non-empty `string`
    +   Falsey values
        +   `0`
        +   `0.0`
        +   `''`
+   Conditions: a boolean expression
+   Block of code
    +   Don't forget colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
+   `if`
+   `else`
+   `elif`
+   `while`
+   `break`
+   `continue`
+   `for`
+   `range()`
    +   `range(n)`: `0`, `1`, ..., `n-1`
    +   `range(start,stop)`: `start`, `start+1`, ..., `stop-1`
        +   Math: `[start,stop)`
    +   `range(start,stop,step)`
        +   If `step` is positive: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step < stop`.
        +   If `step` is negative: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step > stop`.
        +   If `step` is zero: cause a `ValueError`
+   Nested loops
+   `ctrl`+`C` to stop your (buggy) program
+   Practice Question: [Chapter 2]https://automatetheboringstuff.com/chapter2/)
+   Previous task 2: Draw a tree with branches
+   Previous task 3: Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)

### Function

+   `def your_function()`
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
+   `def your_function_with_parameter(parameter)`
    +   Argument
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   [Example](lec10-3.py)
    +   Task: modify the above example to draw a tree like [this](https://scratch.mit.edu/projects/115838437/)
+   Keyword argument
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
    +   We will teach you how to declare function with keyword arguments later.
+   Please do not overwrite the arguments in your function now. We will discuss what will happen if you do so later.
+   Scope
    +   Variables are defined by assignment statements
    +   Global
        +   Defined in global scope
        +   `global`
            +   `global some_var`: `some_var` in this function is the global `some_var`
            +   You must do this if you're going to write global variables
    +   Local
        +   Defined in local scope
    +   Principles
        +   Local variables cannot be used globally.
        +   A local scope cannot access local variables in other scopes.
        +   A local variable and a global variable may have the same name, but only local variable can be accessed.
        +   You may still read the global variable correctly if no local variable is using the same name.

### Guess a number

+   Guess a secret number from `0` to `9`
+   `5` chances

### Bulls and Cows

+   [Wikipedia](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   The `i`-th charactor of a string `x`: `x[i]`
    +   Zero base
