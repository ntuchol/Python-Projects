import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
         if(other == None):
            return False
         if(not isinstance(other, Node)):
            return False
         return self.freq == other.freq

def calculate_frequencies(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    return frequencies

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_node = Node(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)

    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encoding(text):
    if not text:
        return "", {}

    frequencies = calculate_frequencies(text)
    huffman_tree = build_huffman_tree(frequencies)
    codes = generate_codes(huffman_tree)

    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

text = "hello world"
encoded_text, codes = huffman_encoding(text)

print("Encoded text:", encoded_text)
print("Huffman codes:", codes)
