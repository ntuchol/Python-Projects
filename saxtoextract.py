import xml.sax

class ConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.configuration = {}  # Dictionary to store extracted configuration
        self.current_element = ""

    def startElement(self, name, attrs):
        self.current_element = name

    def characters(self, content):
        if self.current_element:
            if self.current_element in self.configuration:
                self.configuration[self.current_element] += content.strip() 
            else:
                self.configuration[self.current_element] = content.strip()

    def endElement(self, name):
        self.current_element = ""

xml_content = """
<configuration>
    <database type="mysql">
        <host>localhost</host>
        <port>3306</port>
        <username>admin</username>
        <password>secret</password>
    </database>
    <api_key>YOUR_API_KEY</api_key>
</configuration>
"""

parser = xml.sax.make_parser()

# Set the custom handler
handler = ConfigHandler()
parser.setContentHandler(handler)

# Parse the XML content (you can also parse a file)
xml.sax.parseString(xml_content, handler)

# Access the extracted configuration
print(handler.configuration)
