class AVLNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"Node({self.key}, {self.value})"


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        self.update_height(node)

        balance_factor = self.get_balance_factor(node)

        if balance_factor > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance_factor < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance_factor > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance_factor < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True

        if abs(self.get_balance_factor(node)) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)
from collections import Counter

class Multiset(Counter):
    def __init__(self, iterable=None):
        super().__init__(iterable)
    
    def add(self, element, count=1):
        self[element] += count
        if self[element] <= 0:
            del self[element]

    def remove(self, element, count=1):
         self.add(element, -count)

    def __repr__(self):
        items_repr = ', '.join(f'{repr(k)}: {v}' for k, v in self.items())
        return f'Multiset({{{items_repr}}})'
import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
         if not node:
            return 0
         return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3
        
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1:
            if data < root.left.data:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if data > root.right.data:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root
    
    def delete(self, root, data):
        if not root:
            return root
        
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            min_right = self.min_value_node(root.right)
            root.data = min_right.data
            root.right = self.delete(root.right, min_right.data)

        self.update_height(root)
        balance = self.balance_factor(root)

        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root
    
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, data):
        if not root or root.data == data:
            return root
        if data < root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

def measure_time(func, *args, num_runs=100):
    total_time = 0
    for _ in range(num_runs):
        start_time = timeit.default_timer()
        func(*args)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / num_runs

if __name__ == "__main__":
    input_sizes = [100, 1000, 10000]
    for size in input_sizes:
        data = random.sample(range(size * 
