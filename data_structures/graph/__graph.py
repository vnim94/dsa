from re import L
from linked_list.stack import Stack
from linked_list.queue import Queue

class DirectedGraph:
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

        while not nodes.isEmpty():
            node = nodes.poll()
            links = self.nodes[node]
            for link in links:
                nodes.add(link)
            values.append(node)

        return values

    def hasPath(self, src, dst):
        nodes = Queue()
        nodes.add(src)

        while not nodes.isEmpty():
            node = nodes.poll()
            links = self.nodes[node]
            for link in links:
                if link == dst:
                    return True
                nodes.add(link)
            
        return False

    def toString(self):
        return self.nodes

class UndirectedGraph:
    def __init__(self):
        self.nodes = {}
    
    def insert(self, *value):
        for v in value:
            if v not in self.nodes:
                self.nodes[v] = []
    
    def link(self, A, B):
        self.nodes[A].append(B)
        self.nodes[B].append(A)

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
            if node not in values:
                values.append(node)
                links = self.nodes[node]
                for link in links:
                    nodes.push(link)

        return values

    def bfs(self, start):
        values = []
        if len(self.nodes) == 0:
            return values

        nodes = Queue()
        nodes.add(start)

        while not nodes.isEmpty():
            node = nodes.poll()
            if node not in values:
                values.append(node)
                links = self.nodes[node]
                for link in links:
                    nodes.add(link)
        
        return values

    def hasPath(self, src, dst):
        visited = {}
        nodes = Queue()
        nodes.add(src)

        while not nodes.isEmpty():
            node = nodes.poll()
            if node not in visited:
                visited[node] = 1
            links = self.nodes[node]
            for link in links:
                if link == dst:
                    return True
                if link not in visited:
                    nodes.add(link)
            
        return False

    def countLinkedNodes(self):
        count = 0
        visited = {}
        
        for node in self.nodes:
            if node not in visited:
                nodes = Queue()
                nodes.add(node)
                
                while not nodes.isEmpty():
                    n = nodes.poll()
                    for link in self.nodes[n]:
                        if link not in visited:
                            visited[link] = 1
                            nodes.add(link)

                count += 1

        return count

    def toString(self):
        return self.nodes
