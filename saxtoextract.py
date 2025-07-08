import xml.sax

class ConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.configuration = {}  # Dictionary to store extracted configuration
        self.current_element = ""

    def startElement(self, name, attrs):
        self.current_element = name
        # You can access attributes using the 'attrs' object (which behaves like a dictionary)
        # For example, if you want to extract a specific attribute, you could do:
        # if name == "database":
        #     self.configuration['db_type'] = attrs.get('type')

    def characters(self, content):
        # Handle the character data within an element
        if self.current_element:
            if self.current_element in self.configuration:
                self.configuration[self.current_element] += content.strip() # Append content if element appears multiple times
            else:
                self.configuration[self.current_element] = content.strip()

    def endElement(self, name):
        # Clear the current element when its end tag is encountered
        self.current_element = ""

# Example XML content (replace with your actual XML file)
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

# Create a SAX parser
parser = xml.sax.make_parser()

# Set the custom handler
handler = ConfigHandler()
parser.setContentHandler(handler)

# Parse the XML content (you can also parse a file)
xml.sax.parseString(xml_content, handler)

# Access the extracted configuration
print(handler.configuration)