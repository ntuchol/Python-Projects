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
        if not self.head:  
            self.head = new_node
            return
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:  
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:  
                    current.prev.next = current.next
                else:  # If it's the head node
                    self.head = current.next
                if current.next:  
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()  
dll.delete(10)
dll.display() 
