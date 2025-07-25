from bs4 import BeautifulSoup

def parse_html_dictionary(html_content):
    
    soup = BeautifulSoup(html_content, 'html.parser')
    dictionary = {}
    for p in soup.find_all('p'):
        b_tag = p.find('b')
        if b_tag:
            word = b_tag.text.strip()
            definition = p.text.replace(b_tag.text, '').strip()
            dictionary[word] = definition
    return dictionary

if __name__ == '__main__':
    html_content = """
    <p><b>Word1</b> Definition of word 1.</p>
    <p><b>Word2</b> Definition of word 2.</p>
    <p><b>Word3</b> Definition of word 3.</p>
    """

    dictionary = parse_html_dictionary(html_content)
    print(dictionary)

    search_word = "Word2"
    if search_word in dictionary:
        print(f"The definition of '{search_word}' is: {dictionary[search_word]}")
    else:
        print(f"'{search_word}' not found in the dictionary.")
