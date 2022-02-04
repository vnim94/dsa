from linkedList import SinglyLinkedList

def findMiddle(head):
    
    # initialise pointers
    slow = head
    fast = head
    # loop until fast = None
    while fast != None and fast.next != None:
        # increment slow by 1
        slow = slow.next
        # increment fast by 2
        fast = fast.next.next
    
    # return slow.data
    return slow.data

list = SinglyLinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)

print(findMiddle(list.head)) # 3

list.insert(6)
print(findMiddle(list.head)) # 4

list.insert(7)
print(findMiddle(list.head)) # 4

