import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {e}")
        return None

if __name__ == '__main__':
    url = "YOUR_FAVORITE_WORD_PAGE_URL"  # Replace with the actual URL
    extracted_text = extract_text_from_url(url)

    if extracted_text:
        print(extracted_text)