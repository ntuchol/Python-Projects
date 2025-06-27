class Node:
    """Represents a node in a tree."""
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def tree_to_nested_string(node):
    """
    Recursively converts a tree structure into a nested string
    representation using parentheses.

    Args:
        node: The current node being processed.

    Returns:
        A string representing the nested structure of the tree.
    """
    if node is None:
        return ""  # Base case for empty tree

    if not node.children:  # Base case for a leaf node (no children)
        return str(node.value)

    # Recursive step: Process the current node and its children
    result = str(node.value) + "("
    for i, child in enumerate(node.children):
        result += tree_to_nested_string(child)
        if i < len(node.children) - 1:  # Add comma between children
            result += ","
    result += ")"

    return result

# Example usage:
# Create a sample tree
root = Node("A", [
    Node("B", [
        Node("D"),
        Node("E")
    ]),
    Node("C", [
        Node("F")
    ])
])

# Convert the tree to a nested string
nested_representation = tree_to_nested_string(root)
print(nested_representation)