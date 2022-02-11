class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, *value):
        for v in value:
            if self.head == None:
                self.head = Node(v)
                self.tail = self.head
            else:
                node = Node(v)
                self.tail.next = node
                self.tail = node

    def toString(self):
        node = self.head
        string = ''
        while node != None:
            string += str(node.data)
            string += ' '
            node = node.next

        return string