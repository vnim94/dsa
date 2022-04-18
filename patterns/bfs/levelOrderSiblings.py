class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    output = []
    if root == None:
        return output

    nodes = [root]
    # iterate until queue empty
    while len(nodes) > 0:
        level = len(nodes)
        # empty level and add # at end
        for i in range(level):
            node = nodes.pop(0)
            output.append(node.data)
            # if reached end of level, set next as None, else set next as next node in queue
            if level - 1 - i == 0:
                node.next = None
            else:
                node.next = nodes[0]
            
            # add children
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
        output.append('#')

    # return output
    return output

def connectAll(root):
    if root == None:
        return None

    nodes = [root]
    # iterate until queue empty
    while len(nodes) > 0:
        level = len(nodes)
        # empty level and add # at end
        for i in range(level):
            node = nodes.pop(0)
            # if reached end of level, set next as None, else set next as next node in queue
            if level - 1 - i > 0:
                node.next = nodes[0]
            
            # add children
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
        # connect to next level
        if len(nodes) > 0:
            node.next = nodes[0]

    # return output
    return root

# tree = Node(1)
# tree.left = Node(2)
# tree.left.left = Node(4)
# tree.left.right = Node(5)
# tree.right = Node(3)
# tree.right.left = Node(6)
# tree.right.right = Node(7)

# print(connect(tree))
# [-1, '#', 0, 1, '#', 2, 3, 4, 5, '#', 6, 7, 8, 9, 10, 11, 12, 13, '#']

tree = Node(-1)
tree.left = Node(0)
tree.left.left = Node(2)
tree.left.left.left = Node(6)
tree.left.left.right = Node(7)
tree.left.right = Node(3)
tree.left.right.left = Node(8)
tree.left.right.right = Node(9)
tree.right = Node(1)
tree.right.left = Node(4)
tree.right.left.left = Node(10)
tree.right.left.right = Node(11)
tree.right.right = Node(5)
tree.right.right.left = Node(12)
tree.right.right.right = Node(13)

# print(connect(tree))
# [1,#,2,3,#,4,5,6,7,#]

root = connectAll(tree)
while root != None:
    print(root.data, end=' ')
    root = root.next


