class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_before(self, target_node, new_data):
        if self.head is None:
            return  # Empty list, nothing to insert before

        if self.head == target_node:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next == target_node:
                new_node = Node(new_data)
                new_node.next = target_node
                current.next = new_node
                return
            current = current.next