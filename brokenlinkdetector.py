import requests
from bs4 import BeautifulSoup
import concurrent.futures

def get_broken_links(url):
    root_domain = url.split("//")[1].split("/")[0]
    broken_links = []

    def validate_url(url_to_check):
        try:
            r = requests.head(url_to_check, timeout=5)
            if r.status_code >= 400:
                broken_links.append(f"{r.status_code} - {url_to_check}")
        except requests.exceptions.RequestException:
             broken_links.append(f"Timeout/Connection Error - {url_to_check}")

    try:
        data = requests.get(url, timeout=10).text
        soup = BeautifulSoup(data, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        
        internal_links = [link for link in links if link.startswith('/') or root_domain in link]
        external_links = [link for link in links if not link.startswith('/') and root_domain not in link]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(validate_url, internal_links + external_links)
            
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to {url} - {e}")
        return
    
    if broken_links:
        print("Broken links found:")
        for link in broken_links:
            print(link)
    else:
        print("No broken links found.")

if __name__ == "__main__":
    url_to_check = input("Enter the URL to check: ")
    get_broken_links(url_to_check)