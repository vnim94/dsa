def findAllMissing(array):
    
    i = 0
    # loop until correct value in place
    while i < len(array):
        # if not in correct position and value at correct position is different, swap
        if array[i] - 1 != i and array[i] != array[array[i] - 1]:
            temp = array[i]
            array[i] = array[temp - 1]
            array[temp - 1] = temp
        # else, skip
        else:
            i += 1 

    # loop and record values where value - 1 != index
    missing = []
    for i in range(len(array)):
        if array[i] - 1 != i:
            missing.append(i + 1)

    # return array
    return missing

print(findAllMissing([2, 3, 1, 8, 2, 3, 5, 1])) #[4, 6, 7], The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
print(findAllMissing([2, 4, 1, 2])) # 3
print(findAllMissing([2, 3, 2, 1])) # 4