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
        self.array[index] = value

    def get(self, key):
        index = self.hash(key)
        return self.array[index]

    def remove(self, key):
        index = self.hash(key)

        self.array.pop(index)

    