import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print("-" * 20)
