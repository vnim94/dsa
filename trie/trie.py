class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Trie:
    def __init__(self):
        self.root = None
        self.pointers = {}

    def insert(self, value):
        if self.root == None:
            self.root = Node(value[0])

    def delete(self):
        None

    def search(self, value):
        None