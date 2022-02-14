class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, *value):
        for v in value:
            if self.top == None:
                self.top = Node(v)
            else:
                node = Node(v)
                node.next = self.top
                self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.data

    def toString(self):
        node = self.top
        string = ''
        while node != None:
            string += str(node.data)
            if node.next != None:
                string += ' -> '
            node = node.next

        return string