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
            if self.right != None:
                if self.right.root == value:
                    if self.right.left != None:
                        self.right = self.right.left
                    elif self.right.right != None:
                        self.right = self.right.right
                    else:
                        self.right = None
                else:
                    self.right.remove(value)
        else:
            if self.left != None:
                if self.left.root == value:
                    if self.left.left != None:
                        self.left = self.left.left
                    elif self.left.right != None:
                        self.left = self.left.right
                    else:
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

    def min(self):
        if self.left == None:
            return self.root
        return self.left.min()

    def max(self):
        if self.right == None:
            return self.root
        return self.right.max()
    
    def height(self):
        None

    def preOrderTraversal(self):
        None

    def inOrderTraversal(self):
        None

    def postOrderTraversal(self):
        None