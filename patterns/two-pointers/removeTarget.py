def removeTarget(array, target):
    
    # initialise index pointers: one to iterate (iterator), one to track non-target and shift numbers (tracker)
    iterator = 0
    tracker = 0
    # loop array using iterator
    while iterator < len(array):
        # if iterator != target
        if array[iterator] != target:
            # set tracker as iterator
            array[tracker] = array[iterator]
            # increment tracker
            tracker += 1
        # increment iterator
        iterator += 1
   
    # return tracker
    return tracker


print(removeTarget([3, 2, 3, 6, 3, 10, 9, 3], 3)) # 4
print(removeTarget([2, 11, 2, 2, 1], 2)) # 2