from xml.dom.minidom import parse, parseString

# Assuming you have an XML file named 'config.xml' with configuration information
# For example:
# <configuration>
#   <setting name="database_url">localhost:5432</setting>
#   <setting name="username">admin</setting>
#   <setting name="password">secret</password>
# </configuration>

try:
    # Parse the XML file
    dom = parse('config.xml')

    # Get the root element
    root = dom.documentElement

    # Get all the 'setting' elements
    settings = root.getElementsByTagName('setting')

    # Extract configuration information
    config = {}
    for setting in settings:
        name = setting.getAttribute('name')
        value = setting.firstChild.nodeValue.strip()
        config[name] = value

    # Print the extracted configuration
    print(config)

except Exception as e:
    print(f"Error parsing XML file: {e}")