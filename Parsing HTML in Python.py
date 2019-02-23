import urllib.request

from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://in.mail.yahoo.com/").read()
html = BeautifulSoup(page,"html.parser")
print(html.title.string)
print(html.get_text())
for link in html.find_all(True):
    print(link.name)
    print(html.find_all('script'))
    print(html.prettify())
    print(html.find_all(["li", "ul"]))
