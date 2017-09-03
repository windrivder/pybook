> 记录 Python 爬虫中常用的库

# urllib/urllib2

```python
from urllib2 import urlopen         # python2
from urllib.request import urlopen  # python3

urlopen(url, data, timeout)
```

# BeautifulSoup

在写爬虫的时候，思考代码的总体格局，让代码既可以捕捉异常又容易阅读。以下代码来自 Python 网络数据采集：

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), "html.parser")
        title = bs_obj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print('Title could not be found')
else:
    print(title)
```

BeautifulSoup 中的四种对象：

- BeautifulSoup
- Tag
- NavigableString
- Comment

```python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
bsObj.findAll("", {"class":"green"})
```
