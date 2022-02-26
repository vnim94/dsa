class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # add to back of queue
    def add(self, value):
        # if empty, add to head
        if self.head == None:
            self.head = Node(value)
        # else, add to tail
        else:
            if self.head.next == None:
                self.head.next = Node(value)
                self.tail = self.head.next
            else:
                self.tail.next = Node(value)
                self.tail = self.tail.next
        self.length += 1

    # remove from front of queue
    def remove(self):
        if self.head.next != None:
            self.head = self.head.next  
        else:
            self.head = None

        self.length -= 1

    # return front of queue
    def peek(self):
        return self.head.data

    # remove and return front of queue
    def poll(self):
        head = self.head.data
        
        if self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next

        self.length -= 1

        return head

    def size(self):
        return self.length

