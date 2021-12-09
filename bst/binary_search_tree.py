class BinarySearchTree:
    def __init__(self, data=None):
        self.root = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.root == None:
            self.root = value
        elif value > self.root:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
    def remove(self, value):
        if self.root == value:
            self.root = None
        elif value > self.root:
            if self.right.root == value:
                self.right = None
            else:
                self.right.remove(value)
        else:
            if self.left.root == value:
                self.left = None
            else:
                self.left.remove(value)

    def search(self, value):
        if self.root == value:
            return True
        if value > self.root:
            if self.right != None:
                return self.right.search(value)
            else:
                return False
        else:
            if self.left != None:
                return self.left.search(value)
            else:
                return False

    def preOrderTraversal(self):
        None

    def inOrderTraversal(self):
        None

    def postOrderTraversal(self):
        None