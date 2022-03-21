from turtle import right
from data_structures.binaryTree import Node

def rightView(root):
    result = []
    # if root is empty, return []
    if root == None:
        return result

    nodes = [root]
    # iterate until queue empty
    while len(nodes) > 0:
        # empty level, but only first node.data to result
        for i in range(len(nodes)):
            # add node.data to result
            node = nodes.pop(0)
            if i == 0:
                result.append(node.data)
            # add right child, else left child
            if node.right != None:
                nodes.append(node.right)
            if node.left != None:
                nodes.append(node.left)

    # return result
    return result

tree = None
print(rightView(tree)) # []

tree = Node(1)
tree.right = Node(3)

print(rightView(tree)) # [1,3]

tree = Node(1)
tree.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(3)
tree.right.right = Node(4)

print(rightView(tree)) # [1,3,4]

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)

print(rightView(tree)) # [1,3,4]
