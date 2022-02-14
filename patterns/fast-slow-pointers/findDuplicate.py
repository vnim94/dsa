def _findDuplicate(array):
    
    # initialise pointers
    slow = array[0]
    fast = array[slow]
    
    # loop until slow = fast
    while slow != fast:
        slow = array[slow]
        fast = array[array[fast]]

    # find cycle length
    current = array[array[slow]]
    length = 1
    while current != array[slow]:
        current = array[current]
        length += 1

    # find start of cycle (start slow at 0, fast at length, loop until slow = fast, return value)
    pointerA = array[0]
    pointerB = array[0]
    
    while length > 0:
        pointerB = array[pointerB]
        length -= 1
    
    while pointerA != pointerB:
        pointerA = array[pointerA]
        pointerB = array[pointerB]

    return pointerA

def findDuplicate(array):

    # initialise pointers. treat values in the array as pointers
    slow = array[0]
    fast = array[slow] # ?
    
    # find where slow meets fast
    while slow != fast:
        slow = array[slow]
        fast = array[array[fast]] # ?

    # find start of cycle
    slow = 0
    while slow != fast:
        slow = array[slow]
        fast = array[fast]

    # return slow
    return slow

print(findDuplicate([1, 4, 4, 3, 2])) # 4
print(findDuplicate([2, 1, 3, 3, 5, 4])) # 3
print(findDuplicate([2, 4, 1, 4, 4])) # 4