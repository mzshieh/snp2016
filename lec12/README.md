## Lecture 12

### IoTtalk

+   Real devices!
+   Take photos
+   Feedback

### Debugger

+   IDLE
    +   Debug
        +   Toggle Debugger
+   [More Information](https://inventwithpython.com/chapter7.html)

### Review

+   Download [this](lec12-1.py) first
+   How to complete 2-digit Bull and Cow?
    +   Prepare the answer
        +   Method 1: generate a valid answer
            +   Might be very complex
        +   Method 2: Repeat generating candidates until a valid one
            +   Might be time consuming
        +   Other method?
    +   Get a valid guess
        +   What is valid? 
            +   A guess should be a 2-digit number having different digits.
                +   Length is 2
                    +   `if` + `len()`
                +   Is a number
                    +   `try` + `except` + `int()`
                +   In the range [0,99]
                    +   `if` + `<` + `and`
                +   Have two different digits
                    +   `if` + `// 10` + `% 10`
    +   Compute `A` and `B`
        +   Implemenmt functions
        +   Prepare a variable storing the value `ret` to be returned
    +   End the game if the player is correct
        +   Add `else` statement to break the `for` loop

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
+   `len()`
+   `in`
    +   Operator
    +   `for` loop
+   `not in`
+   Auto boxing & auto unboxing
    +   [code](../lec11/lec11-3.py)
+   Task: Write another program to help you win!
    +   [2-digit version helper](lec12-2.py)
    +   [4-digit version Game](lec12-3.py)

### More about Lists

+   Negative index: `some_list[-1]`
+   Sublists with slices: try `print([0,1,2,3,4][1:3])`
    +   Inclusive, exclusive
+   Concatenation `+`
+   Replication `*`
+   Delete an element of certain position:`del`
+   `index()`
    +   try `print([0,1,2,0].index(0))`
+   `insert(pos,val)`: insert `val` to position `pos`
    +   Let `a = [0,1,2]`. What will happen if we perform `a.insert(1,3)`?
+   `remove(val)`: remove an element of value `val`
    +   Let `a = [1,0,0,1]`. What will happen if we perform `a.remove(1)`?
+   `sort()`: sort the list ascendingly