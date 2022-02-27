class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

        self.length += 1

    def pop(self):
        if self.top:
            top = self.top
            self.top = self.top.next
            self.length -= 1
            return top.data

    def peek(self):
        if self.top:
            return self.top.data 

    def isEmpty(self):
        return self.top == None

    def size(self):
        return self.length
    