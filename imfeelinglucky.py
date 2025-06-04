
import webbrowser, bs4, requests, sys
 
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?source=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())
 
# Retreive top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
 
# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))