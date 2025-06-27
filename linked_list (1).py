Here’s an example of a Doubly Linked List implementation in Python. A doubly linked list allows traversal in both forward and backward directions, with each node containing pointers to both its previous and next nodes.

Copy the code
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:  # If the list is empty
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:  # If it's not the head node
                    current.prev.next = current.next
                else:  # If it's the head node
                    self.head = current.next
                if current.next:  # If it's not the tail node
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

# Example usage:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()  # Output: 5 <-> 10 <-> 20
dll.delete(10)
dll.display()  # Output: 5 <-> 20

Key Features:
append(data): Adds a new node at the end of the list.
prepend(data): Adds a new node at the beginning of the list.
delete(data): Removes the first node with the specified data.
display(): Prints the list in a readable format.

This implementation is simple yet flexible, and you can expand it further based on your needs!
