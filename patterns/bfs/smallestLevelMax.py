class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def smallestLevelMax(root):
    nodes = [root]
    level = 1
    smallest = None
    max = None
    # iterate until queue empty
    while len(nodes) > 0:
        sum = 0
        # empty queue (i.e level)
        for i in range(len(nodes)):            
            node = nodes.pop(0)
            # add to sum
            sum += node.data
            # add children
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
                
        # if sum > max, set max and record level
        if max == None or sum > max:
            max = sum
            smallest = level

        # increment level
        level += 1
        
    # return level
    return smallest

tree = Node(1)
tree.left = Node(7)
tree.right = Node(0)
tree.left.left = Node(7)
tree.left.right = Node(-8)

print(smallestLevelMax(tree))