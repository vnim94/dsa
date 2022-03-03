from data_structures.linkedList import LinkedList

def rotate(head, k):
    
    current = head
    # link end to start
    while current.next != None:
        current = current.next

    current.next = head

    current = head
    i = 0
    # loop until k (k becomes last node)
    while i != k:
        current = current.next
        i += 1

    # set head as k.next
    head = current.next

    # set k.next as None
    current.next = None

    # return head
    return head

list = LinkedList()
list.insert(0, 1, 2)

list.head = rotate(list.head, 4) 
print(list.toString()) # 2, 0, 1

list = LinkedList()
list.insert(1, 2, 3, 4, 5)

list.head = rotate(list.head, 2) # 4, 5, 1, 2, 3
print(list.toString())