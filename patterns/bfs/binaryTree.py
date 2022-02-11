class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data == None:
            self.data = value
        else:
            if value > self.data:
                if self.right == None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
            else:
                if self.left == None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)