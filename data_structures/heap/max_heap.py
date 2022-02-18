class Heap:
    def __init__(self):
        self.nodes = []
        
    def insert(self, value):
        self.nodes.append(value)

        index = len(self.nodes) - 1
        if index % 2 == 0:
            parent = (index - 2) // 2
        else:
            parent = (index - 1) // 2
        
        while self.nodes[index] > self.nodes[parent]:

            temp = self.nodes[parent]
            self.nodes[parent] = self.nodes[index]
            self.nodes[index] = temp

    
    def delete(self):
        # set root equal to last node
        last = len(self.nodes) - 1
        self.nodes[0] = self.nodes[last]
        del self.nodes[last]

        root = 0
        
        while True:
            
            # get index of left and right child
            left = root * 2 + 1
            right = root * 2 + 2

            # if left and right child exist, swap largest with root
            if left < last and right < last:
                if self.nodes[left] < self.nodes[right]:
                    largest = right
                else:
                    largest = left

                if self.nodes[root] < self.nodes[largest]:
                    temp = self.nodes[root]
                    self.nodes[root] = self.nodes[largest]
                    self.nodes[largest] = temp
                    root = largest
            # if only left child and larger than root, swap with root
            elif left < last and not right < last and self.nodes[root] < self.nodes[left]:
                temp = self.nodes[root]
                self.nodes[root] = self.nodes[left]
                self.nodes[left] = temp
                root = left
            # if only right child and larger than root, swap with root
            elif not left < last and right < last and self.nodes[root] < self.nodes[right]:
                temp = self.nodes[root]
                self.nodes[root] = self.nodes[right]
                self.nodes[right] = temp
                root = right
            else:
                break