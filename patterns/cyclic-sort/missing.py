def findMissingNumber(array):
    i = 0
    # loop until correct value in correct position
    while i < len(array):
        if array[i] < len(array) and array[i] != i:
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