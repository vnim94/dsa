from binaryTree import Node

def hasPath(root, s):
    
    # exit condition: if node is a leaf node & value = s, return True. 
    if root.left == None and root.right == None and root.data == s:
        return True

    # check left and right sub-trees for s - node.data
    if root.left != None and hasPath(root.left, s - root.data):
        return True
    if root.right != None and hasPath(root.right, s - root.data):
        return True

    return False

tree = Node()

print(hasPath(tree, 0)) # false

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

print(hasPath(tree, 5)) # false

tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.right = Node(1)

print(hasPath(tree, 22)) # true
