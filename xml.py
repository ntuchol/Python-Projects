import xml.etree.ElementTree as ET

xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book category="fiction">
        <title lang="en">The Great Gatsby</title>
        <author>F. Scott Fitzgerald</author>
        <year>1925</year>
    </book>
    <book category="non-fiction">
        <title lang="en">Sapiens: A Brief History of Humankind</title>
        <author>Yuval Noah Harari</author>
        <year>2014</year>
    </book>
    <book category="fiction">
        <title lang="en">To Kill a Mockingbird</title>
        <author>Harper Lee</author>
        <year>1960</year>
    </book>
</library>
root = ET.fromstring(xml_data)

print(f"Root tag: {root.tag}")
print("\nLibrary Books:")
for book in root.findall('book'):
    category = book.get('category')
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text

    print(f"  Category: {category}")
    print(f"    Title: {title}")
    print(f"    Author: {author}")
    print(f"    Year: {year}")
    print("-" * 20)

print("\nSearching for a fiction book:")
for book in root.findall('.//book[@category="fiction"]'):
    title = book.find('title').text
    print(f"  Found Fiction Book: {title}")
