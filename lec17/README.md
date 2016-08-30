## Lecture 17

## Review

### `requests`

+   `import requests`: don't forget `s`
+   URL: 網址
    +   Absolute: `https://github.com/mzshieh/snp2016`
    +   Relative: `../lec14/lec14-1.py`
+   Reference: [HTTP](https://chino.taipei/note-%E5%B8%B8%E8%A6%8B%E7%9A%84HTTP-Method%E7%9A%84%E4%B8%8D%E5%90%8C%E6%80%A7%E8%B3%AA%E5%88%86%E6%9E%90%EF%BC%9AGet-Post%E5%92%8C%E5%85%B6%E4%BB%964%E7%A8%AEMethod%E7%9A%84%E5%B7%AE%E5%88%A5/)
+   `result = requests.get(URL)`：這是一個 `request.models.Response`，這我們還不會直接拿來用。
+   `result.text`: 這才是拿回來的東西，是`str`。這我們會用。
    +   `len(result.text)`: 取回來的資料大小。
+   `result.raise_for_status()`: 如果連線有狀況，透過這個處理。
+   Save the content
    +   Create directories
        +   `import os`
        +   `os.makedirs(path)`
    +   Open a file to save it: `the_file = open('a_name', 'wb')`
        +   Filename: `a_name`
        +   Mode: `wb` means "write binary"
            +   `the_file.write(chunk)`: write a chunk of `bytes`
    +   `for chunk in result.iter_content(102400):` to iterate 102400-byte chunks of `result`
    +   Remember to close the file: `the_file.close()`
    +   Sample [code](../lec14/lec14-1.py)

### Beautiful soup

+   [Sample code](lec17.py)
+   `from bs4 import BeautifulSoup`
+   Parsing HTML: the real webpages
    +   View source!
+   `soup = BeautifulSoup(result.text,'lxml')`
    +   try `soup = BeautifulSoup(result.text,'html.parser')` if you are unable to use `lxml`
+   `soup.find(tag)`
    +   Get a `Tag` from the html
    +   Try `type(soup.find('html'))`
+   Get information from `Tag`: use `.get()`
    +   `.get()` is safer than `[]`
+   `find_all(tag)` returns a list
+   `soup.find(tag,attr=value)`
    +   Advanced `find` usage
        +   Accessing attributes
            +   keyword argument
            +   `dictionary`
+   CSS selector: `select(tag)`
    +   Get all `tag`s
    +   Return a list
    +   Similar to `find_all`
    +   Special attribute: `class` and `id`
        +   Use `requests` to get `https://tw.news.yahoo.com/sports/` and cook `soup`
        +   `class` use `.` : Try `soup.select('div.yom-mod.yom-blist')`
        +   `id` use `#`: Try `soup.select('div#mediamegatron')`
+   Redo Task: open five webpages
    +   Tag: `a`
    +   Attribute: `href`
    +   `endswith('html')`
    +   `import webbrowser`
+   Task: Open five images in browser
    +   Tag: `img`
    +   Attribute: `src`
+   Task: Save five images from some webpage
+   Task: Crawl the [Yahoo Sport News](https://tw.news.yahoo.com/sports/)
    +   找出五條新聞，並選出報導中的第一句話。
        +   Hint: `<p class="first">`
    +   Bonus: 擷取報導附圖。