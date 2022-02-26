from linked_list.stack import Stack
from linked_list.queue import Queue

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

    def dfs(self, start):
        values = []
        if len(self.nodes) == 0:
            return values 
        
        nodes = Stack()
        nodes.push(start)

        while not nodes.isEmpty():
            node = nodes.pop()
            links = self.nodes[node]
            for link in links:
                nodes.push(link)
            values.append(node)

        return values

    def bfs(self, start):
        values = []
        if len(self.nodes) == 0:
            return values

        nodes = Queue()
        nodes.add(start)

        while nodes.head != None:
            node = nodes.poll()
            links = self.nodes[node]
            for link in links:
                nodes.add(link)
            values.append(node)

        return values

    def hasPath(self, src, dst):
        if dst in self.dfs(src):
            return True
        return False

    def toString(self):
        return self.nodes

    