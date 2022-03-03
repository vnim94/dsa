from data_structures.binaryTree import Node
from data_structures.queue import Queue

def traverse(root):
    result = []
    # add root
    nodes = Queue()
    nodes.push(root)

    # loop while queue not empty
    while not nodes.isEmpty():
        # empty current queue
        length = nodes.length
        level = []

        for _ in range(length):
            node = nodes.pop()

            # add node value to result
            level.append(node.data)

            # if node has children, add to queue
            if node.left != None:
                nodes.push(node.left)
            if node.right != None:
                nodes.push(node.right)

        result.insert(0, level)

    # return result
    return result

tree = Node(3)
tree.left = Node(9)
tree.left.left = Node(4)
tree.left.right = Node(6)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(traverse(tree)) # [[4, 6, 15, 7], [9, 20], [3]]