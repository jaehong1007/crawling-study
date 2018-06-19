from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime
random.seed(datetime.datetime.now())

# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bs0bj = BeautifulSoup(html.read(), "html.parser")
#         title = bs0bj.body.h1
#     except AttributeError as e:
#         return None
#
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bs0bj = BeautifulSoup(html, "html.parser")
# # nameList = bs0bj.findAll("span", {"class":"green"})
# # for name in nameList:
# #     print(name.get_text())
# images = bs0bj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print(image["src"])

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bs0bj = BeautifulSoup(html, "html.parser")
# for link in bs0bj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bs0bj = BeautifulSoup(html, "html.parser")
    return bs0bj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    # for link in bs0bj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)