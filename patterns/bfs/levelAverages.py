from data_structures.queue import Queue
from data_structures.binaryTree import Node

def levelAverages(root):
    
    # create result array
    averages = []
    # add root to queue
    nodes = Queue()
    nodes.push(root)
    
    # loop until queue is empty
    while not nodes.isEmpty():
        divisor = 0
        sum = 0

        # empty queue, calculate average for the level
        for _ in range(nodes.length):
            node = nodes.pop()
            
            # increment sum and number of nodes of the level
            sum += node.data
            divisor += 1

            # add children to queue
            if node.left != None:
                nodes.push(node.left)
            if node.right != None:
                nodes.push(node.right)

        averages.append(sum / divisor)
        
    # return result 
    return averages

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(levelAverages(tree)) # [3, 14.5, 11]

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.left.left = Node(15)
tree.left.right = Node(7)

print(levelAverages(tree)) # [3, 14.5, 11]