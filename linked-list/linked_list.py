class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    # get -> return value at index
    def get(self, index):
        
        # start at head
        if index == 0:
            return self.head.data

        value = self.head

        # loop through to specified index and set value as node
        for _ in range(index):
            value = value.next

        # return data at the node
        return value.data

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
        
        node = self.head

        # go to last node
        while node.next != None:
            node = node.next

        # if current node empty, insert value, else insert new node
        if node.data == None:
            node.data = value
        else:
            node.next = Node(value)

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
    