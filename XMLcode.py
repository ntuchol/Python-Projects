import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Iterate through the XML structure
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print("-" * 20)