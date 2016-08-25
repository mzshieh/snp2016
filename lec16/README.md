## Lecture 16

## Review

### `requests`

+   `import requests`: don't forget `s`
+   URL: 網址
+   `result = requests.get(URL)`
+   `result.text`: 這才是拿回來的東西
+   `result.raise_for_status()`: 如果連線有狀況，透過這個處理。
+   Save the content
    +   Open a file to save it: `the_file = open('a_name', 'wb')`
        +   Filename: `a_name`
        +   Mode: `wb` means "write binary"
            +   `the_file.write(chunk)`: write a chunk of bytes
            +   `the_file.write(str.encode())`
    +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
    +   Remember to close the file: `the_file.close()`
    +   Sample [code](../lec14/lec14-1.py)
    +   Reference: [HTTP](https://chino.taipei/note-%E5%B8%B8%E8%A6%8B%E7%9A%84HTTP-Method%E7%9A%84%E4%B8%8D%E5%90%8C%E6%80%A7%E8%B3%AA%E5%88%86%E6%9E%90%EF%BC%9AGet-Post%E5%92%8C%E5%85%B6%E4%BB%964%E7%A8%AEMethod%E7%9A%84%E5%B7%AE%E5%88%A5/)

### Web Browser

+   `import webbrowser` then use `webbrowser.open(URL)` to open the page

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
    +   You may also use slice on `list`
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
+   Redo Task: open five webpages
    +   Tag: `a`
    +   Attribute: `href`
+   Task: Open five images in browser
    +   Tag: `img`
    +   Attribute: `src`
+   Task: Save five images from some webpage
+   Task: Crawl the [NCTU bulletin system](https://infonews.nctu.edu.tw)