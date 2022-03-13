from data_structures.binaryTree import Node

def zigzag(root):
    result = []
    # if root is empty, return []
    if root.data == None:
        return result
    
    nodes = [root]
    leftToRight = True
    # iterate until queue is empty
    while len(nodes) > 0:
        level = []
        # empty level
        for _ in range(len(nodes)):
            node = nodes.pop(0)
            # left to right -> add value to end
            if leftToRight:
                level.append(node.data)
            # right to left -> add value to start
            else:
                level.insert(0, node.data)
            # add children
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        result.append(level)

        # reverse direction
        leftToRight = not leftToRight

    # return result
    return result

tree = Node()
print(zigzag(tree)) # []

tree = Node(1)
print(zigzag(tree)) # [[1]]

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(zigzag(tree)) # [[3],[20,9],[15,7]]

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.right = Node(5)

print(zigzag(tree)) # [[1],[3,2],[4,5]]