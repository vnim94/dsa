from data_structures.binaryTree import Node

def traverse(root): 
    nodes = [root]
    result = []

    while len(nodes) > 0:
        node = nodes.pop()
        result.append(node.data)
        
        if node.right != None:
            nodes.append(node.right)
        
        if node.left != None:
            nodes.append(node.left)

    return result


tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.right = Node(1)

print(traverse(tree)) # [5,4,11,7,2,8,13,4,1]