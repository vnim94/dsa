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

    def delete(self, value):
        node = self.root
        for char in value:
            node = node.pointers[char]

        node.end = False

    def search(self, value):
        node = self.root
        for char in value:
            if char in node.pointers:
                node = node.pointers[char]
            else:
                return False

        if node.end:
            return True
        return False