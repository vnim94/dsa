class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HashTable:
    def __init__(self):
        self.array = [None] * 10

    def hash(self, value):
        value = str(value)
        hashSum = 0
        for i in range(len(value)):
            hashSum += ord(value[i]) + 1
            hashSum *= ord(value[i]) + 1
            hashSum -= ord(value[i]) + 1
        hashSum %= 10

        return hashSum

    def put(self, key, value):
        index = self.hash(key)
        node = Node([key,value])
        if self.array[index] != None:
            node.next = self.array[index]
        self.array[index] = node

    def get(self, key):
        index = self.hash(key)
        if self.array[index]:
            node = self.array[index]
            while node != None:
                if node.data[0] == key:
                    return node.data[1]
                node = node.next
            

    def remove(self, key):
        index = self.hash(key)

        self.array.pop(index)

    