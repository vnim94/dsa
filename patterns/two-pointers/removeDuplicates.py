def removeDuplicates(array):

    # initialise index pointers, one to iterate (pointerA) and one to track non-duplicates and swap numbers (pointerB)
    pointerA = 1
    pointerB = 1

    # loop through array using pointerA
    while pointerA < len(array):
        # if pointerA != pointerB - 1
        if array[pointerA] != array[pointerB - 1]:
            # set value at pointerB as value at pointerA
            array[pointerB] = array[pointerA]
            # increment pointerB   
            pointerB += 1

        pointerA += 1

    # return pointerB
    return pointerB

print(removeDuplicates([2, 3, 3, 3, 6, 9, 9])) # 4
print(removeDuplicates([2, 2, 2, 11])) # 2
