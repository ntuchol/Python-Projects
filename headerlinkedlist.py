class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert(header, x):
    curr = header
    while curr.next is not None:
        curr = curr.next

    new_node = Node(x)
    curr.next = new_node

def print_list(header):
    curr = header.next
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    header = Node(0)
    insert(header, 1)
    insert(header, 2)
    insert(header, 3)
    insert(header, 4)

    print_list(header)
