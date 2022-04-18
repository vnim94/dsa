def removeDuplicates(array):

    # initialise index pointers, one to iterate (iterator) and one to track non-duplicates and swap numbers (tracker)
    iterator = 1
    tracker = 1

    # loop through array using iterator
    while iterator < len(array):
        # if iterator != tracker - 1
        if array[iterator] != array[tracker - 1]:
            # set value at tracker as value at iterator
            array[tracker] = array[iterator]
            # increment tracker   
            tracker += 1

        iterator += 1
    
    # return tracker
    return tracker

print(removeDuplicates([2, 3, 3, 3, 6, 9, 9])) # 4
print(removeDuplicates([2, 2, 2, 11])) # 2
print(removeDuplicates([1,1,1,2,2,3])) # 3
