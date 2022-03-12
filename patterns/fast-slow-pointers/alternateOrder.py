from re import L
from data_structures.linkedList import LinkedList

def alternateOrder(head):
    # find middle of list using fast and slow pointers
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    # reverse from middle onwards
    while slow != None:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    # iterate until prev is none
    while prev != None:
        # link node in left to node in right
        next = head.next
        head.next = prev
        head = next

        next = prev.next
        prev.next = head
        prev = next

    if head != None: # after reverse, end of left points to head of right. therefore, need to break cycle
        head.next = None

list = LinkedList()
list.insert(2,4,6,8,10,12)

alternateOrder(list.head)
print(list.toString()) # 2 -> 12 -> 4 -> 10 -> 6 -> 8
