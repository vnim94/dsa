from __queue__ import Queue
from binaryTree import BSTNode

def traverse(root):
    result = []
    # record node.data
    result.append(root.data)
    
    # use queue to store visited nodes
    nodes = Queue()
    
    # store children in queue
    if root.left != None:
        nodes.push(root.left)

    if root.right != None:
        nodes.push(root.right)
    
    # loop through queue until empty
    while not nodes.isEmpty():
        # pop queue
        node = nodes.pop()
        
        # if node has children, add to queue
        if node.left != None:
            nodes.push(node.left)
        
        if node.right != None:
            nodes.push(node.right)

        # add node.data
        result.append(node.data)

    # return array  
    return result

tree = BSTNode()
tree.insert(12)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(10)
tree.insert(5)

print(traverse(tree))
