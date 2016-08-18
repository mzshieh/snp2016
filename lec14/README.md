## Lecture 14

## Review

### Comments on Lists

+   Empty list: `[]`
+   May have elements of different types
+   Access (zero-based) `i`-th element of `list x`: `x[i]`
+   The elements are mutable (modifiable)
+   `append()`
+   `len()`
+   `in`
    +   Operator
    +   `for` loop
    +   `[i**2 for i in range(10)]`
+   `sort()`: sort the list ascendingly
+   Mutable things versus immutable things
    +   Variables like boxes: we may put something into it via `=` (assignment).
        +   If there is already something in the box (assigned to the variable), then just dump the old things.
    +   Immutable things like balls: you may not change its content.
    +   Mutable things like "smaller" boxes: you may change its content.
        +   Put more balls and boxes into it.
        +   We may also dump the old things and put new things into the smaller box.
        +   Use corresponding functions or "assignments"

### Dictionary

+   `list` is indexed by `int`
    +   From `0` to `len()-1`
+   Dictionary is indexed by keys (words).
    +   `mz = {'Name': 'MZ', 'Height': 178, 'Weight': 108}`
    +   Word: key
    +   Definition: value
    +   A set of key-value pairs
+   Empty dictionary: `{}`
+   `keys()`: like a list of keys (words)
+   `values()`: like a list of values (definition)
+   `items()`: like a list of key-value pairs
+   `in`: work for "keys" (words)
+   Prevent errors from indexing a missing key
    +   `get(key,val)`: If `key` is missing, then return `val`
    +   `setdefault(key,val)`: if there is no such `key`, initialize the key-value pair to `(key,val)` and return `val`. Otherwise return the value corresponding `key`.

### Function definition
+   `def fn(arg,*arg_list,**arg_dict):`
+   Unlimited number of positional argument: using list
    +   Use `[]`
+   Keyword argument: using dictionary!
    +   Use `get()`

### `pyautogui`

+   We were blind.
+   [Sample code 1](../lec13/lec13-1.py)
+   `screenshot()`
+   `getpixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](../lec13/lec13-2.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Task: Check all boxes!
    +   Practice [here](https://goo.gl/forms/dr5mkE7Z9dKiJ3gI3)
    +   Join [Cloud9](https://c9.io/) NCTU Team
        +   Get your own server for term project!
+   Task: Make your tree drawing program
    +   Some complex branches: [code](../lec13/lec13-3.py)
    +   More readable: use `def` block
    +   Less dependent on maximizing window
        +   Use screen shot and `locateOnScreen`
        +   Use dictionary to handle the filenames

### `requests`

+   A website has different looks
    +   When transfering its content, it looks like a sequence of bytes
    +   A sequence of bytes? A sequence of characters? A string.
    +   We need a different kind of eyes
+   `import requests`: don't forget `s`
+   URL: Uniform Resource Locator
    +   這術語好長我們叫他網址好了
+   `result = requests.get('https://raw.githubusercontent.com/mzshieh/snp2016/master/README.md')`
    +   這網址好長請試著複製貼上吧
+   `result.text`
    +   這內容好字串：`type(result.text)`
    +   String processing
        +   `str`
        +   `import re`: regular expression
+   `result.raise_for_status()`
    +   連網頁做了好多事情，要是網址有錯瀏覽器會直接當掉給你看嗎？
    +   It is OK to raise an exception, but always using `try-except` blocks is tedious.
        +   Java is tedious: almost always `try` or `throws` (`raise` in Python)
    +   `raise_for_status()`: If there is any exception, raise it now.
+   Save the content
    +   Open a file to save it: `the_file = open('a_name.html', 'wb')`
        +   Filename: `a_name`
        +   Mode: `wb` means "write binary"
            +   `the_file.write(chunk)`: write a chunk of bytes
        +   Mode: `wt` means "write text"
            +   `the_file.write(some_str)`: write a string
    +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
    +   Remember to close the file: `the_file.close()`
    +   Sample [code](lec14-1.py)

### String processing

+   Escape Characters: [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
+   Multiline Strings: triple quotes ```   
+   Indexing:
    +   `print('123'[0])`
    +   `print('123'[-1])`
+   `index()`
    +   `print('123123123'.index('312'))`
+   Slicing: 
    +   `print('abcde'[2:])`
    +   `print('abcde'[:2])`
    +   `print('abcde'[1:3])`
+   `in` and `not in`
    +   `print('abc' in 'zabcy')`
    +   `print('gg' not in 'zabcy')`
+   `upper()` and `lower()`
+   `isupper()`, `islower()`, `isdecimal()`, `isalpha()`, `isalnum()`
    +   try `'123.0'.isdecimal()`
+   `join(list_str)`
    +   try `', '.join([str(i) for i in range(10)])`
+   `split(string)`
    +   try `'<a href="https://automatetheboringstuff.com/">'.split('"')`
+   `startswith(string)` and `endswith(string)`
    +   Many URLs start with `http` and end with `html`
+   `strip()`, `rstrip()`, `lstrip()`
+   Task: open all URLs which end with `html` in a wikipedia page.
    +   `import webbrowser` then use `webbrowser.open(URL)` to open the page
+   [Supplement](https://chino.taipei/note-%E5%B8%B8%E8%A6%8B%E7%9A%84HTTP-Method%E7%9A%84%E4%B8%8D%E5%90%8C%E6%80%A7%E8%B3%AA%E5%88%86%E6%9E%90%EF%BC%9AGet-Post%E5%92%8C%E5%85%B6%E4%BB%964%E7%A8%AEMethod%E7%9A%84%E5%B7%AE%E5%88%A5/)