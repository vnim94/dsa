class Node:
    def __init__(self, data):
        self.data = data
        self.end = False
        self.pointers = {}

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, value):
        node = self.root
        for char in value:
            if char not in node.pointers:
                node.pointers[char] = Node(char)
            node = node.pointers[char]

        node.end = True

    def delete(self):
        None

    def search(self, value):
        None