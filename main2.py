class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_iterative(self):
        """Traverses the linked list iteratively and prints the data of each node."""
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_recursive(self, node):
         """Traverses the linked list recursively and prints the data of each node."""
         if node is None:
            return
         print(node.data, end=" ")
         self.traverse_recursive(node.next)

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def peek(self):
      if self.is_empty():
          return None
      return self.head.data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def remove_last(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def peek_first(self):
      return self.head.data if self.head else None
    
    def peek_last(self):
      return self.tail.data if self.tail else None

    def get_size(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Deque is empty"
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node