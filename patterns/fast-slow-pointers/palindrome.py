from re import L
from data_structures.linkedList import LinkedList

def palindrome(head):
    # find middle using fast and slow pointers
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse from middle onwards
    current = slow
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    # compare left and right using fast and slow pointers
    while prev:
        # if diff, return False
        if prev.data != head.data:
            return False
        head = head.next
        prev = prev.next

    # return True
    return True

list = LinkedList()
list.insert(1, 2, 2, 1)

print(palindrome(list.head)) # true

list = LinkedList()
list.insert(1, 2)

print(palindrome(list.head)) # false
