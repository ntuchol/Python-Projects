class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_depth(node):
    if node is None:
        return 0
    else:
        left_depth = tree_depth(node.left)
        right_depth = tree_depth(node.right)

        return max(left_depth, right_depth) + 1