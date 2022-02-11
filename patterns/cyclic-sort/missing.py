def findMissingNumber(array):
    i = 0
    # loop until correct value in correct position
    while i < len(array):
        # if value == max value, skip
        if array[i] == len(array):
            i += 1
        else:
            # value != index, swap with value at index, else skip
            if array[i] != i:
                temp = array[i]
                array[i] = array[temp]
                array[temp] = temp
            else:
                i += 1
            
    # loop 
    for i in range(len(array)):
        # if value != index, return index
        if array[i] != i:
            return i

print(findMissingNumber([4, 0, 3, 1])) # 2
print(findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1])) # 7