from data_structures.linkedList import LinkedList

def reverse(head, start, end):
    
    # if start = end, return head
    if start == end:
        return head

    current = head
    prev = None

    # 1. go to start of sublist
    while current != None and current.data < start:
        prev = current
        current = current.next

    beforeStart = prev
    startNode = current

    # 2. reverse the sublist
    while current != None and current.data <= end:
        next = current.next
        # reverse pointer  
        current.next = prev
        prev = current
        current = next

    afterEnd = current
        
    # 3. connect afterEnd
    startNode.next = afterEnd

    # 4. if beforeStart = None, set prev as head. Else, connect beforeStart 
    if beforeStart == None:
        head = prev
    else:
        beforeStart.next = prev

    return head

list = LinkedList()
list.insert(1, 2, 3, 4, 5)

list.head = reverse(list.head, 2, 4)

print(list.toString()) # 1 4 3 2 5


