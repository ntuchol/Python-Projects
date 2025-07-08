import urllib.parse

def url_parser(url):
    """
    Parses a URL and returns a dictionary of its components.

    Args:
        url (str): The URL to parse.

    Returns:
        dict: A dictionary containing the parsed URL components, or None if parsing fails.
    """
    try:
        parsed_url = urllib.parse.urlparse(url)
        return {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': parsed_url.query,
            'fragment': parsed_url.fragment
        }
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None

if __name__ == '__main__':
    test_url = "https://www.example.com/path/to/resource?param1=value1&param2=value2#section1"
    parsed_components = url_parser(test_url)

    if parsed_components:
        for key, value in parsed_components.items():
            print(f"{key}: {value}")