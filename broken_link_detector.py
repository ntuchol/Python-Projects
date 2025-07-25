import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def find_broken_links(base_url):
    broken_links = []
    visited_urls = set()

    def crawl_page(url):
        if url in visited_urls:
            return
        visited_urls.add(url)

        try:
            response = requests.get(url)
            if response.status_code >= 400:
                broken_links.append((url, response.status_code))
                return 

            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)
                
                if urlparse(absolute_url).netloc == urlparse(base_url).netloc:
                    crawl_page(absolute_url)

        except requests.exceptions.RequestException as e:
            broken_links.append((url, str(e)))

    crawl_page(base_url)
    return broken_links

