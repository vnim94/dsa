class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def findLength(head):
    # initialise pointers
    slow = head
    fast = head

    # loop until end reached or overlap
    while fast != None:
        # increment slow
        slow = slow.next
        # increment fast
        fast = fast.next.next
        # if slow = fast, return start
        if slow == fast:
            return calculateLength(slow)

    # return 0 if no cycle
    return 0

def calculateLength(slow):
    node = slow
    length = 0

    while True:
        node = node.next
        length += 1
        
        if node == slow:
            break

    return length

linkedList = Node(1)
linkedList.next = Node(2)
linkedList.next.next = Node(3)
linkedList.next.next.next = Node(4)
linkedList.next.next.next.next = Node(5)
linkedList.next.next.next.next.next = Node(6)
# print(findLength(linkedList)) # 0

linkedList.next.next.next.next.next.next = linkedList.next.next
print(findLength(linkedList)) # 4

linkedList.next.next.next.next.next.next = linkedList.next.next.next
print(findLength(linkedList)) # 3