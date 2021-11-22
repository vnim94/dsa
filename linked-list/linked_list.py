class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # get -> return value at index
    def get(self, index):
        
        # start at head
        if index == 0:
            return self.head.data

        node = self.head

        # loop through to specified index and set value as node
        for _ in range(index):
            node = node.next

        # return data at the node
        return node.data

    # contains -> return true if value exists, else false
    def contains(self, value):
        # start at head
        node = self.head

        if node.data == value:
            return True

        # loop until next is None
        while node.next != None:
            node = node.next
            if node.data == value:
                return True

        return False

    # add -> add value at end of list
    def add(self, value):
        # if empty, insert at head and set next as tail
        if self.head == None:
            self.head = Node(value)
        elif self.head.next == None:
            self.tail = Node(value)
            self.head.next = self.tail
        # else set as tail
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode


    # insert -> add value at specified index 
    def insert(self, index, value):
        
        node = self.head

        # create new node
        newNode = Node(value)

        if index == 0:
            newNode.next = node
            self.head = newNode
        else:
            # go to node before index
            i = 0
            while i < index - 1:
                node = node.next
                i += 1

            # insert new node 
            newNode.next = node.next
            node.next = newNode

    # set -> update value at specified index
    def set(self, index, value):

        node = self.head

        if index == 0:
            node.data = value
        else:
            # go to node
            i = 0
            while i < index:
                node = node.next
                i += 1

            node.data = value

    # push -> insert value at beginning of list
    def push(self,value):
        
        # create new node
        newNode = Node(value)

        # set newNode.next to head
        newNode.next = self.head

        # set newNode as head
        self.head = newNode

    # pop -> remove last element in list
    def pop(self):
        node = self.head
        
        # go to node before last and set next to None
        while node.next.next != None:
            node = node.next

        node.next = None

    # remove -> remove specified index
    def remove(self, index):
        node = self.head
        i = 0
        # go to node before index
        while i < index - 1:
            node = node.next
            i += 1
        # node.next = node.next.next
        if node.next.next != None:
            node.next = node.next.next
        else:
            node.next = None

    # size -> returns length of list
    def size(self):
        node = self.head
        i = 1
        while node.next != None:
            node = node.next
            i += 1

        return i

    # return string represntation of linked list
    def __str__(self):
        string = ''

        node = self.head

        while node.next != None:
            string += str(node.data) + ' -> '
            node = node.next

        string += str(node.data)
        
        return string
    