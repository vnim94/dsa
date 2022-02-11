def findAllDuplicates(array):
    
    i = 0
    # loop
    while i < len(array):
        # if out of place and value at correct place not the same, swap 
        if array[i] - 1 != i and array[i] != array[array[i] - 1]:
            temp = array[i]
            array[i] = array[temp - 1]
            array[temp - 1] = temp
        # else skip
        else:
            i += 1

    duplicates = []

    # loop and store duplicates
    for i in range(len(array)):
        if array[i] - 1 != i:
            duplicates.append(array[i])

    # return duplicates
    return duplicates

print(findAllDuplicates([3, 4, 4, 5, 5])) # [4, 5]
print(findAllDuplicates([5, 4, 7, 2, 3, 5, 3])) # [3, 5]