from data_structures.binaryTree import Node

def hasPath(root, s):
    # exit condition: if node is a leaf node & value = s, return True. 
    if root.left == None and root.right == None and root.data == s:
        return True

    # check left and right sub-trees for s - node.data
    if root.left != None and hasPath(root.left, s - root.data):
        return True
    if root.right != None and hasPath(root.right, s - root.data):
        return True

    return False

def hasPathIteratively(root, target):
    if root.data == None:
        return False
    # if root.data = s, return true
    if root.data == target:
        return True

    nodes = [root]
    sum = 0
    # iterate until stack is empty
    while len(nodes) > 0:
        # pop top, set as prev and add to sum
        node = nodes.pop()
        sum += node.data
        # if leaf node -> if sum = target, return true, else minus from sum
        if node.left == None and node.right == None:
            if sum == target:
                return True
            sum -= node.data
        # add right child
        if node.right != None:
            nodes.append(node.right) 
        # add left child
        if node.left != None:
            nodes.append(node.left)

    # return false
    return False

tree = Node()

print(hasPath(tree, 0), '-', hasPathIteratively(tree, 0)) # false

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

print(hasPath(tree, 5), '-', hasPathIteratively(tree, 5)) # false

tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right = Node(8)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.right = Node(1)

print(hasPath(tree, 22), '-', hasPathIteratively(tree, 22)) # true