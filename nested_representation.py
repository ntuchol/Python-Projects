class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def tree_to_nested_string(node):
    
    if node is None:
        return ""  

    if not node.children:
        return str(node.value)

    result = str(node.value) + "("
    for i, child in enumerate(node.children):
        result += tree_to_nested_string(child)
        if i < len(node.children) - 1:  
            result += ","
    result += ")"

    return result

root = Node("A", [
    Node("B", [
        Node("D"),
        Node("E")
    ]),
    Node("C", [
        Node("F")
    ])
])

nested_representation = tree_to_nested_string(root)
print(nested_representation)
