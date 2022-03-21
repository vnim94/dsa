from data_structures.binaryTree import Node

def sumAllPaths(root):
    None

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

print(sumAllPaths(tree)) # 25

tree = Node(4)
tree.left = Node(9)
tree.right = Node(0)
tree.left.left = Node(5)
tree.left.right = Node(1)

print(sumAllPaths(tree)) # 1026

