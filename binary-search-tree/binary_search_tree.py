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
        if self.root == None:
            return
        if value > self.root and self.right:
            self.right = self.right.remove(value)
            return self
        elif value < self.root and self.left:
            self.left = self.left.remove(value)
            return self
        else:
            # no children
            if self.left == None and self.right == None:
                return None
            # one child
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            # two children - find max in left subtree, replace current node value with max value and delete node with max
            current = self
            node = self.left
            while node.right != None:
                current = node
                node = node.right
            self.root = node.root
            current.right = None
            
            return self
            

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

    def isValid(self, lowerBound=None, upperBound=None):
        if self.root == None:
            return True

        if self.left:
            self.left.isValid(None, self.root)
        if self.right:
            self.right.isValid(self.root, None)
        else:
            if upperBound != None:
                if self.root <= upperBound:
                    return True
                return False
            if lowerBound != None:
                if self.root > lowerBound:
                    return True
                return False

        return True

        