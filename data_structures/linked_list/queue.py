class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    # add to back of queue
    def add(self, value):
        # if empty, add to front
        if self.front == None:
            self.front = Node(value)
        # else, add to back
        else:
            if self.front.next == None:
                self.front.next = Node(value)
                self.back = self.front.next
            else:
                self.back.next = Node(value)
                self.back = self.back.next
        self.length += 1

    # remove from front of queue
    def remove(self):
        if self.front.next != None:
            self.front = self.front.next  
        else:
            self.front = None

        self.length -= 1

    # return front of queue
    def peek(self):
        return self.front.data

    # remove and return front of queue
    def poll(self):
        front = self.front.data
        
        if self.front.next == None:
            self.front = None
        else:
            self.front = self.front.next

        self.length -= 1

        return front

    def size(self):
        return self.length

    def isEmpty(self):
        return self.front == None

