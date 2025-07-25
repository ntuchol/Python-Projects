from xml.dom.minidom import parse, parseString

try:
    dom = parse('config.xml')

    root = dom.documentElement

    settings = root.getElementsByTagName('setting')

    config = {}
    for setting in settings:
        name = setting.getAttribute('name')
        value = setting.firstChild.nodeValue.strip()
        config[name] = value

    print(config)

except Exception as e:
    print(f"Error parsing XML file: {e}")
