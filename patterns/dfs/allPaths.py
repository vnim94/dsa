from binaryTree import Node

def allPaths(root):
    
    # base case: leaf node -> return [node.data]
    if root.left == None and root.right == None:
        return [[root.data]]

    # store paths in array
    paths = []

    # traverse left and right child
    if root.left != None:
        result = allPaths(root.left)
        for path in result:
            path.insert(0, root.data)
        paths += result

    if root.right != None:
        result = allPaths(root.right)
        for path in result:
            path.insert(0, root.data)
        paths += result
    
    # return paths
    return paths

tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.left = Node(5)
tree.right.right.right= Node(1)

print(allPaths(tree)) # [[5, 4, 11, 7], [5, 4, 11, 2], [5, 8, 13], [5, 8, 4, 5], [5, 8, 4, 1]]   

