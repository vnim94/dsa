from data_structures.binaryTree import Node
from data_structures.queue import Queue

def levelMax(root):
    
    # create result array
    result = []
    # add root to queue
    nodes = Queue()
    nodes.push(root)

    # loop until queue is empty
    while not nodes.isEmpty():
        max = None
        # empty queue, record max
        for _ in range(nodes.length):
            node = nodes.pop()
            if max == None:
                max = node.data
            if node.data > max:
                max = node.data

            # add children of node to queue
            if node.left != None:
                nodes.push(node.left)
            if node.right != None:
                nodes.push(node.right)

        # record max for the level
        result.append(max)

    # return result
    return result

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.left.left = Node(15)
tree.left.right = Node(7)

print(levelMax(tree)) # [3, 20, 15]