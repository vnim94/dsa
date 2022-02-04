class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, *value):
        for v in value:
            if self.head == None:
                self.head = Node(v)
                self.tail = self.head
            else:
                newNode = Node(v)
                self.tail.next = newNode
                self.tail = newNode
