from data_structures.linkedList import LinkedList

def reverse(head):
        
    current = head
    prev = None

    # loop until current = None
    while current != None:
        # set next = current.next
        next = current.next
        # reverse pointer
        current.next = prev
        # set prev = current
        prev = current
        # set current = next
        current = next
    
    return prev

def reverseRecursively(head, prev = None):
    # base case: if head is None, return prev
    if head == None:
        return prev
    # set next
    next = head.next
    # reverse pointers
    head.next = prev
    # return recurse using next as head, and head as prev
    return reverseRecursively(next, head)

list = LinkedList()
list.insert(2, 4, 6, 8, 10)
list.head = reverse(list.head)

print(list.toString())

list = LinkedList()
list.insert(2, 4, 6, 8, 10)
list.head = reverseRecursively(list.head)

print(list.toString())
