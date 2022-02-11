from linkedList import LinkedList

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
    
    head = prev

    return head

list = LinkedList()
list.insert(2, 4, 6, 8, 10)
list.head = reverse(list.head)

print(list.toString())