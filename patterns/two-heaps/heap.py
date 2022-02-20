class MinHeap:
    def __init__(self):
        self.nodes = []
        self.count = 0

    def insert(self, value):
        self.nodes.append(value)
        self.count += 1

        index = self.count - 1
        if index % 2 == 0:
            parent = (index - 2) // 2
        else:
            parent = (index - 1) // 2

        while self.nodes[index] < self.nodes[parent]:
            self.nodes[index], self.nodes[parent] = self.nodes[parent], self.nodes[index]

    def remove(self):
        last = self.count - 1
        root = self.nodes[0]
        self.nodes[0] = self.nodes[last]
        del self.nodes[last]
        self.count -= 1

        parent = 0

        while True:
            left = parent * 2 + 1
            right = parent * 2 + 2

            if left < last and right < last:
                if self.nodes[left] < self.nodes[right]:
                    smallest = left
                else:
                    smallest = right
                self.nodes[smallest], self.nodes[parent] = self.nodes[parent], self.nodes[smallest]
                parent = smallest
            elif left < last and not right < last and self.nodes[left] < self.nodes[parent]:
                self.nodes[left], self.nodes[parent] = self.nodes[parent], self.nodes[left]
                parent = left
            elif not left < last and right < last and self.nodes[right] < self.nodes[parent]:
                self.nodes[right], self.nodes[parent] = self.nodes[parent], self.nodes[right]
                parent = right
            else:
                break

        return root

class MaxHeap:
    def __init__(self):
        self.nodes = []
        self.count = 0

    def insert(self, value):
        self.nodes.append(value)
        self.count += 1

        index = self.count - 1
        if index % 2 == 0:
            parent = (index - 2) // 2
        else:
            parent = (index - 1) // 2

        while self.nodes[index] > self.nodes[parent]:
            temp = self.nodes[index]
            self.nodes[index] = self.nodes[parent]
            self.nodes[parent] = temp

    def remove(self):
        last = self.count - 1
        root = self.nodes[0]
        self.nodes[0] = self.nodes[last]
        del self.nodes[last]
        self.count -= 1

        parent = 0

        while True:
            left = parent * 2 + 1
            right = parent * 2 + 2

            if left < last and right < last:
                if self.nodes[left] > self.nodes[right]:
                    largest = left
                else: 
                    largest = right
                self.nodes[largest], self.nodes[parent] = self.nodes[parent], self.nodes[largest]
                parent = largest
            elif left < last and not right < last and self.nodes[left] > self.nodes[parent]:
                self.nodes[left], self.nodes[parent] = self.nodes[parent], self.nodes[left]
                parent = left
            elif not left < last and right < last and self.nodes[right] > self.nodes[parent]:
                self.nodes[right], self.nodes[parent] = self.nodes[parent], self.nodes[right]
                parent = right
            else:
                break

        return root