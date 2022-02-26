class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = Node(None)
        
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        top = self.top
        self.top = self.top.next
        return top.data

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top.data == None

    def size(self):
        node = self.top
        i = 0
        while node.next != None:
            node = node.next
            i += 1

        return i
    