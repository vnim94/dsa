class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def hasCycle(head):
    # initialise pointers
    slow = head
    fast = head

    # loop until overlap or end reached (i.e fast pointer is None)
    while fast != None:
        # increment slow by 1
        slow = slow.next
        # increment fast by 2
        fast = fast.next.next

        # if slow = fast -> return true
        if slow == fast:
            return True

    # return false
    return False

linkedList = Node(1)
linkedList.next = Node(2)
linkedList.next.next = Node(3)
linkedList.next.next.next = Node(4)
linkedList.next.next.next.next = Node(5)
linkedList.next.next.next.next.next = Node(6)
print(hasCycle(linkedList)) # false

linkedList.next.next.next.next.next = linkedList.next.next
print(hasCycle(linkedList)) # true

linkedList.next.next.next.next.next = linkedList.next.next.next
print(hasCycle(linkedList)) # true