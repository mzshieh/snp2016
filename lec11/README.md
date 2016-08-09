## Lecture 11

## Review

+   [Slide](snp_lec11.pdf)

### Flow Control

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
    +   Don't forget the colon `:`
    +   Indent: spaces and tabs are allowed
        +   Recommend: 4 spaces
    +   [Slide]()
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
+   Nested blocks
+   `ctrl`+`C` to stop your (buggy) program
+   Practice Question: [Chapter 2](https://automatetheboringstuff.com/chapter2/)
+   Previous task: Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)

### Function

+   `def your_function()`
+   `def your_function_with_parameter(parameter)`
+   `def your_function_with_parameters(parameter1, parameter2)`
+   `return`
    +   The function is terminated either by `return` or by the end of the block.
    +   `None`: if there is no `return` or just `return` nothing
    +   Argument
    +   [Example](lec10-3.py)
    +   Task: modify the above example to draw a tree like [this](https://scratch.mit.edu/projects/115838437/)
+   Keyword argument
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
+   Please do not overwrite the arguments in your function now.
+   Scope
    +   Variables are defined by assignment statements
    +   Local
        +   Defined in local scope
            +   Local scope: `def` statement
            +   In the same function
    +   Global
        +   Defined in global scope
        +   `global`
            +   `global some_var`: `some_var` in this function is the global `some_var`
            +   You must do this if you're going to write global variables
    +   Principles
        +   Local variables cannot be used globally.
        +   A local scope cannot access local variables in other scopes.
        +   A local variable and a global variable may have the same name, but only local variable can be accessed.
        +   You may still read the global variable correctly if no local variable is using the same name.
+   Practice Question: [Chapter 3](https://automatetheboringstuff.com/chapter3/)
+   Previous task: Draw a tree with branches

### Guess a number

+   Guess a secret number from `0` to `9`
+   `5` chances
+   [Code](lec11-1.py)

### Bulls and Cows

+   [Wikipedia](https://en.wikipedia.org/wiki/Bulls_and_Cows)
+   Task: Implement a 2-digit version
    +   [Partial code](lec11-2.py)
+   Task(??): Implement a normal version

### Lists and Tuples

+   `type()`
+   List
    +   Empty list: `[]`
    +   May have elements of different types
        +   `[12, 3.4, None, True, 'string', print]`
    +   Access (zero-based) `i`-th element of `list x`: `x[i]`
        +   try `[123,456][1]`
        +   try `[12, 3.4, None, True, 'string', print][5]('hello world')`
        +   try `[123,456][1.0]`
    +   The elements are mutable (modifiable)
+   Tuple
    +   Empty tuple: `()`
    +   Single element tuple: `(element,)`
        +   try `type(('str'))` and `type(('str',)`
    +   `(12, 3.4, None, True, 'string', print)`
    +   The elements are immutable (not modifiable)
+   `list()` and `tuple()`
    +   Try `list(('a','b','c'))`
    +   Try `tuple(['d','e','f'])`
    +   Try `list('hello')`
    +   Try `tuple('hello')`
+   `append()`
+   `in`
+   `not in`
+   Auto boxing & auto unboxing
    +   [code](lec11-3.py)
+   Try to simplify or to accomplish
    +   Bull and cow: 4-digit version
    +   Draw a tree: more complicated version