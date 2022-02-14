class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def push(self, *value):
        for v in value:
            if self.front == None:
                self.front = Node(v)
                self.back = self.front
            else:
                node = Node(v)
                self.back.next = node
                self.back = node

            self.length += 1

    def pop(self):
        node = self.front
        if self.back == self.front:
            self.back = self.front.next
        self.front = self.front.next
        self.length -= 1
        return node.data

    def isEmpty(self):
        if self.front == None:
            return True
        return False

    def toString(self):
        current = self.front
        string = ''
        while current != None:
            string += str(current.data)
            if current.next != None:
                string += ' -> '
            current = current.next

        return string
