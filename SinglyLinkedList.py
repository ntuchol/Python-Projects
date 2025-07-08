class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_size(self):
        """Calculates and returns the size (number of nodes) of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"The size of the linked list is: {my_list.get_size()}")

empty_list = SinglyLinkedList()
print(f"The size of the empty linked list is: {empty_list.get_size()}")
