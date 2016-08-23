## Lecture 15

## Review

### `pyautogui`

+   We were blind.
+   [Sample code 1](../lec13/lec13-1.py)
+   `screenshot().getpixel()`
    +   `(R,G,B)`
+   How to take a screen shot
    +   Windows: print screen key
        +   Hold alt, then press print screen
            +   This gives you a picture of window on focus
        +   Use Microsoft Paint to save the screenshot into png file
+   [Sample code 2](../lec13/lec13-2.py)
+   `locateOnScreen()`
+   `locateAllOnScreen()`
+   Use smaller patterns!
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
    +   Sample [code](../lec14/lec14-1.py)
    +   Reference: [HTTP](https://chino.taipei/note-%E5%B8%B8%E8%A6%8B%E7%9A%84HTTP-Method%E7%9A%84%E4%B8%8D%E5%90%8C%E6%80%A7%E8%B3%AA%E5%88%86%E6%9E%90%EF%BC%9AGet-Post%E5%92%8C%E5%85%B6%E4%BB%964%E7%A8%AEMethod%E7%9A%84%E5%B7%AE%E5%88%A5/)

### String processing

+   Escape Characters: [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
+   Multiline Strings: triple quotes `'''`   
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
+   Task: open 5 URLs which end with `html` in a wikipedia page.
    +   `import webbrowser` then use `webbrowser.open(URL)` to open the page
    +   Bonus: open 5 random URLs

### Beautiful soup

+   `from bs4 import BeautifulSoup` and using `BeautifulSoup` versus `import bs4` and using `bs4.BeautifulSoup`
+   Parsing HTML: the real webpages
    +   View source!
+   [Example code 1](../crawler/example1.py)
    +   `find(tag)`
        +   Get a `Tag` from the html
        +   Try `type(div)`
+   [Example code 2](../crawler/example2.py)
    +   Get information from `Tag`: use `.get`
    +   `.get` is safer than `[]`
+   [Example code 4](../crawler/example4.py)
    +   `find_all` returns a list
    +   CSS selector: `select(tag)`
        +   Get all `tag`s
        +   Return a list
+   [Example code 3](../crawler/example3.py)
    +   Advanced `find` usage
        +   Accessing attributes
            +   keyword argument
            +   dictionary
    +   Try `soup.select('div.find_by_class')`
+   [Example code 5](../crawler/example5.py)
    +   Try to use `select` to replace `find`
+   Task: Crawl the [NCTU bulletin system](https://infonews.nctu.edu.tw)
+   Task: Open five images in browser
    +   Tag: `img`
    +   Attribute: `src`
+   Task: Save five images from some webpage