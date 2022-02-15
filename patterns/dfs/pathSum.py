from binaryTree import Node

def pathSum(root, target):
    
    # base case: leaf node & node.data = target -> return [[node.data]]
    if root.left == None and root.right == None and root.data == target:
        return [[root.data]]
        
    # array to store paths
    paths = []

    # check left and right child with target - root.data
    if root.left != None:
        result = pathSum(root.left, target - root.data)
        # if result not empty, add root.data to front
        if len(result) > 0:
            for path in result:
                path.insert(0, root.data)
            paths += result
        
    if root.right != None:
        result = pathSum(root.right, target - root.data)
        if len(result) > 0:
            for path in result:
                path.insert(0, root.data)
            paths += result

    return paths

tree = Node(1)

print(pathSum(tree, 1)) # [[1]]

tree = Node(1)
tree.right = Node(2)

print(pathSum(tree, 0)) # []

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

print(pathSum(tree, 4)) # [[1,3]]

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

print(pathSum(tree, 22)) # [[5,4,11,2],[5,8,4,5]]   