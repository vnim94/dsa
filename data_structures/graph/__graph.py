from linked_list.stack import Stack

class Graph:
    def __init__(self):
        self.nodes = {}

    def insert(self, *value):
        for v in value:
            if v not in self.nodes:
                self.nodes[v] = []

    def link(self, nodeA, nodeB):
        self.nodes[nodeA].append(nodeB)

    def contains(self, value):
        if value in self.nodes:
            return True
        return False

    def traverseDepth(self):
        if len(self.nodes) == 0:
            return [] 
        
        nodes = Stack()

        while not nodes.isEmpty():
            node = nodes.pop()



    def toString(self):
        return self.nodes

    