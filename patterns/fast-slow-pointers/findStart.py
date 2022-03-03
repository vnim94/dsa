from data_structures.linkedList import SinglyLinkedList

def findLength(head):
    # initialise pointers
    slow = head
    fast = head

    # loop while fast != None
    while fast != None and fast.next != None:
        # increment slow by 1
        slow = slow.next
        # increment fast by 2
        fast = fast.next.next
        # if slow = fast, calculate length and return value
        if slow == fast:
            return calculateLength(slow)

    # return 0
    return 0

def calculateLength(head):
    node = head
    length = 0
    # loop until head is reached again, increment counter on each loop
    while True:
        node = node.next
        length += 1

        if node == head:
            break
    
    return length

def findStart(head):
    
    # find length
    length = findLength(head)
    # initialise pointers
    A = head
    B = head
    # move fast pointer to length
    for _ in range(length):
        B = B.next
    # loop until slow = fast
    while A != B:
        A = A.next
        B = B.next

    # return slow
    return A.data

list = SinglyLinkedList()
list.insert(1, 2, 3, 4, 5, 6)

list.head.next.next.next.next.next.next = list.head.next.next
print(findStart(list.head)) # 3

list.head.next.next.next.next.next.next = list.head.next.next.next
print(findStart(list.head)) # 4

list.head.next.next.next.next.next.next = list.head
print(findStart(list.head)) # 1