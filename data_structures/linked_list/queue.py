import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = None

    # add to back of queue
    def add(self, value):
        # if empty, add to head
        if self.head.data == None:
            self.head.data = value
        # else, add to tail
        else:
            if self.head.next == None:
                self.head.next = Node(value)
                self.tail = self.head.next
            else:
                self.tail.next = Node(value)
                self.tail = self.tail.next

    # remove from front of queue
    def remove(self):
        if self.head.next != None:
            self.head = self.head.next  
        else:
            self.head = Node(None)

    # return front of queue
    def peek(self):
        return self.head.data

    # remove and return front of queue
    def poll(self):
        head = self.head.data
        
        if self.head.next == None:
            self.head = Node(None)
        else:
            self.head = self.head.next

        return head

    def size(self):
        node = self.head
        i = 1
        while node.next != None:
            node = node.next
            i += 1

        return i

