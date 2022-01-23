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
        for char in value:
            if self.root.pointers[char] != None:
                self.root.pointers[char] = None
                

    def search(self, value):
        node = self.root
        for char in value:
            if char in node.pointers:
                node = node.pointers[char]
            else:
                return False

        return True