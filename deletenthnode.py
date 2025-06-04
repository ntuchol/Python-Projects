class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_nth_node(head, n):
    if not head:
        return None

    if n == 1:
        return head.next

    current = head
    previous = None
    count = 1

    while current and count != n:
        previous = current
        current = current.next
        count += 1

    if not current:
        return head

    previous.next = current.next
    return head