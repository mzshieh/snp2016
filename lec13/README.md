## Lecture 13

## Review
### Debugger

+   IDLE
    +   Debug
        +   Toggle Debugger
+   [More Information](https://inventwithpython.com/chapter7.html)
+   Debugger allows you to inspect the program during execution
+   Breakpoint
+   Step
    +   Into
    +   Over
    +   Out

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
    +   [2-digit version helper](../lec12-2.py)
    +   [4-digit version Game](lec13-0.py)

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
+   Using `for` and `in` to generate a `list`

### Dictionary

+   `list` is indexed by `int`
    +   From `0` to `len()-1`
+   `instructor = {'Name': 'MZ', 'Height': 178, 'Weight': 108}`
    +   try `print(instructor['Name'])`
    +   try `print(instructor['age'])`
+   Dictionary is indexed by keys (words).
    +   Word: key
    +   Definition: value
    +   A set of key-value pairs
+   Empty dictionary: `{}`
+   `keys()`
+   `values()`
+   `items()`
+   `in`
    +   try `print('MZ' in instructor)`
    +   try `print('Name' in instructor)`
    +   try `print(('Name','MZ') in instructor)`
+   `get(key,val)`: If `key` is missing, then return `val`
+   `setdefault(key,val)`: if there is no such `key`, initialize the key-value pair to `(key,val)` and return `val`. Otherwise return the value corresponding `key`.
+   Pretty printing: `pprint`

### Function definition
+   `def fn(arg,*arg_list,**arg_dict):`
+   Unlimited number of positional argument: using list
    +   Use `[]`
+   Keyword argument: using dictionary!
    +   Use `get()`

### `pyautogui`

+   `screenshot()`
+   `pixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
    +   Join [Cloud9](https://c9.io/) NCTU Team
        +   Get your own server for term project!
+   Task: Make your tree drawing program
    +   Some complex branches: [code](lec13-1.py)
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`
        +   Use dictionary to handle the filenames
