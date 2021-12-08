class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # get -> return value at index
    def get(self, index):
        
        if index == 0:
            return self.head.data
        
        if index - 0 < self.length - index:
            node = self.head
            i = 0
            while i < index:
                node = node.next
                i += 1
            return node.data
        else:
            node = self.tail
            i = self.length - 1
            while i > index:
                node = node.prev
                i -= 1
            return node.data

    # contains -> return true if value exists, else false
    def contains(self, value):
        
        if self.head.data == value or self.tail.data == value:
            return True
        
        # start at head
        node = self.head

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

        # increment length
        self.length += 1


    # insert -> add value at specified index 
    def insert(self, index, value):
        
        node = self.head

        # create new node
        newNode = Node(value)

        if index == 0:
            newNode.next = node
            self.head = newNode
        elif index == self.length - 1:
            self.tail.next = newNode
            self.tail = newNode
        else:
            if index - 0 < self.length - index:
                node = self.head
                i = 0
                while i < index:
                    node = node.next
                    i += 1
                
                newNode.next = node
                node = newNode

            else:
                node = self.tail
                i = self.length - 1
                while i > index:
                    node = node.prev
                    i -= 1
                
                newNode.next = node
                node = newNode

        # increment length
        self.length += 1

        print('head: ' + str(self.head.data))
        # print('tail: ' + str(self.tail.data))

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

        # increment length
        self.length += 1

    # pop -> remove last element in list
    def pop(self):
        node = self.head
        
        # go to node before last and set next to None
        while node.next.next != None:
            node = node.next

        node.next = None

        # decrement length
        self.length -= 1

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

        # decrement length
        self.length -= 1

    # reverse
    def reverse(self):
        
        prev = None
        current = self.head
        next = self.head

        # loop until last node
        while current != None:
            next = next.next
            # reverse next pointer
            current.next = prev
            prev = current
            current = next
        
        # set last node as head
        self.head = prev

    # size -> returns length of list
    def size(self):
        return self.length

    # return string represntation of linked list
    def __str__(self):
        string = ''

        node = self.head

        while node.next != None:
            string += str(node.data) + ' -> '
            node = node.next

        string += str(node.data)
        
        return string
    