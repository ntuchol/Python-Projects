import xml.etree.ElementTree as ET
from nltk import Tree

def nltk_tree_to_xml(tree: Tree) -> ET.Element:
    xml_element = ET.Element(tree.label())

    for child in tree:
        if isinstance(child, Tree):  
            xml_element.append(nltk_tree_to_xml(child))
        else:  
            leaf_element = ET.Element(str(child))  
            leaf_element.text = str(child)
            xml_element.append(leaf_element) 

    return xml_element

if __name__ == '__main__':
    nltk_tree = Tree('S', [Tree('NP', ['I']), Tree('VP', [Tree('V', ['enjoyed']), Tree('NP', ['my cookie'])])])
    print("NLTK Tree:")
    print(nltk_tree)

    xml_tree = nltk_tree_to_xml(nltk_tree)

    xml_string = ET.tostring(xml_tree, encoding='unicode')

    print("\nXML Representation:")
    print(xml_string)
