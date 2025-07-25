
import webbrowser, bs4, requests, sys
 
print('Googling...') 
res = requests.get('http://google.com/search?source=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())
 
soup = bs4.BeautifulSoup(res.text, "html.parser")
 
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
