from queue import *

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
                    if self.left.right != None:
                        self.left = self.left.right
                    elif self.left.left != None:
                        self.left = self.left.left
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
        if self.left == None and self.right == None:
            return 0
        if self.left != None and self.right == None:
            return self.left.height() + 1
        if self.right != None and self.left == None:
            return self.right.height() + 1 
        return max(self.left.height(), self.right.height()) + 1

    def levelOrderTraversal(self):
        result = []
        if self.root == None:
            return result

        result.append(self.root)
        discovered = Queue()
        
        if self.left == None and self.right == None:
            return result
        if self.left != None:
            discovered.put(self.left)
        if self.right != None:
            discovered.put(self.right)

        while not discovered.empty():
            node = discovered.get()
            result.append(node.root)
            
            if node.left != None:
                discovered.put(node.left)
            if node.right != None:
                discovered.put(node.right)

        return result

    def preOrderTraversal(self, result=[]):
        
        if self.root == None:
            return result
        
        result.append(self.root)

        if self.left:
            self.left.preOrderTraversal(result)

        if self.right:
            self.right.preOrderTraversal(result)

        return result
                
    def inOrderTraversal(self, result=[]):
        
        if self.root == None:
            return result

        if self.left:
            self.left.inOrderTraversal(result)

        result.append(self.root)

        if self.right:
            self.right.inOrderTraversal(result)

        return result

    def postOrderTraversal(self, result=[]):

        if self.root == None:
            return result

        if self.left:
            self.left.postOrderTraversal(result)
        
        if self.right:
            self.right.postOrderTraversal(result)

        result.append(self.root)

        return result
        