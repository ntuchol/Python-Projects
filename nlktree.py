import xml.etree.ElementTree as ET
from nltk import Tree

def nltk_tree_to_xml(tree: Tree) -> ET.Element:
    """
    Converts an NLTK tree to an XML ElementTree element recursively.

    Args:
        tree: The NLTK tree to convert.

    Returns:
        An xml.etree.ElementTree.Element representing the XML counterpart.
    """
    # Create the root element of the XML tree with the NLTK tree's label
    xml_element = ET.Element(tree.label())

    # Iterate over the children of the NLTK tree
    for child in tree:
        if isinstance(child, Tree):  # If the child is a subtree (another NLTK Tree)
            # Recursively convert the subtree to an XML element and append it
            xml_element.append(nltk_tree_to_xml(child))
        else:  # If the child is a leaf (a non-tree value like a word)
            # Create a new XML element with the leaf's value as the tag name
            # and set its text content to the leaf's value
            leaf_element = ET.Element(str(child))  # Assuming the leaf is a string
            leaf_element.text = str(child)
            xml_element.append(leaf_element)  # Append the leaf element to the parent

    return xml_element

if __name__ == '__main__':
    # Example NLTK Tree
    nltk_tree = Tree('S', [Tree('NP', ['I']), Tree('VP', [Tree('V', ['enjoyed']), Tree('NP', ['my cookie'])])])
    print("NLTK Tree:")
    print(nltk_tree)

    # Convert the NLTK Tree to an XML element
    xml_tree = nltk_tree_to_xml(nltk_tree)

    # Convert the XML element to a string with pretty indentation
    xml_string = ET.tostring(xml_tree, encoding='unicode')

    print("\nXML Representation:")
    print(xml_string)
