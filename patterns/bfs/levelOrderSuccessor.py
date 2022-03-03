from data_structures.queue import Queue
from data_structures.binaryTree import Node

def levelOrderSuccessor(root, value):
    # if root.data = value, return None
    if root.data == value:
        return None
    
    nodes = Queue()
    nodes.push(root)

    # iterate until queue empty
    while not nodes.isEmpty():
        node = nodes.pop()
        # if node.data = value and level not empty, return next node
        if node.data == value and nodes.length > 0:
            return nodes.pop().data
        # add children
        if node.left != None:
            nodes.push(node.left)
        if node.right != None:
            nodes.push(node.right)

    # return None
    return None

root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)

print(levelOrderSuccessor(root, 12)) # None
print(levelOrderSuccessor(root, 9)) # 10