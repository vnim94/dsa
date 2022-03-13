from data_structures.binaryTree import Node

def minDepth(root):
    if root == None:
        return 0

    nodes = [root]
    depth = 1
    # iterate until queue empty
    while len(nodes) > 0: 
        # empty level
        for _ in range(len(nodes)):
            node = nodes.pop(0)
            # if leaf node, return depth
            if node.left == None and node.right == None:
                return depth
            # add children
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        # increment depth
        depth += 1


    # return depth
    return depth

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(minDepth(tree)) # 2

tree = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.right.right = Node(5)
tree.right.right.right.right = Node(6)

print(minDepth(tree)) # 5