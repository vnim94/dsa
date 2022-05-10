from data_structures.binaryTree import Node

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

def allPathsIteratively(root):
    nodes = [root]
    paths = []
    path = []
    parent = root
    # iterate while stack not empty
    while len(nodes) > 0:
        # pop top and add to path
        node = nodes.pop()
        path.append(node.data)
        # if leaf node, add path to paths
        if node.left == None and node.right == None:
            paths.append(path.copy())
            path.pop()
            # TODO
            while len(path) > 1 and (parent.left and path[-1] != parent.left.data) and (parent.right and path[-1] != parent.right.data):
                path.pop()
            continue
        # set parent
        parent = node

        # add right
        if node.right != None:
            nodes.append(node.right)
        # add left
        if node.left != None:
            nodes.append(node.left)

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

# print(allPaths(tree), '-', allPathsIteratively(tree)) 
print(allPathsIteratively(tree))

# ["5->4->11->7", "5->4->11->2", "5->8->13", "5->8->4->5", "5->8->4->1"]
# [[5, 4, 11, 7], [5, 4, 11, 2], [5, 8, 13], [5, 8, 4, 5], [5, 8, 4, 1]]   

