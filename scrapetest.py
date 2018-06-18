from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(), "html.parser")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
