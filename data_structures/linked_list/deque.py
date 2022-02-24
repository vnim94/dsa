class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def addLast(self, *value):
        for v in value:
            if self.front == None:
                self.front = Node(v)
                self.back = self.front
            else:
                node = Node(v)
                self.back.next = node
                self.back = node
            self.length += 1

    def addFirst(self, *value):
        for v in value:
            if self.front == None:
                self.front = Node(v)
                self.back = self.front
            else:
                node = Node(v)
                node.next = self.front
                self.front = node
            self.length += 1
                
    def removeFirst(self):
        node = self.front
        self.front = self.front.next
        return node.data

    def removeLast(self):
        node = self.front
        while node != self.back:
            prev = node
            node = node.next
        self.back = prev
        return node.data
        
    