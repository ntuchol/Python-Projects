import xml.etree.ElementTree as ET

def read_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("Root tag:", root.tag)
        for child in root:
            print("Tag:", child.tag, "| Attributes:", child.attrib)
    except Exception as e:
        print("Error reading XML file:", e)

read_xml("example.xml")

from bs4 import BeautifulSoup

def read_html(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            print("Title:", soup.title.string if soup.title else "No title found")
            print("First 5 links:")
            for link in soup.find_all("a", limit=5):
                print("Link:", link.get("href"))
    except Exception as e:
        print("Error reading HTML file:", e)

read_html("example.html")
