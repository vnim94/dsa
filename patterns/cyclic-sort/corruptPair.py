def findCorruptPair(array):
    i = 0
    # sort the array (loop in same spot until value in correct place)
    while i < len(array):
        # if value != index + 1, swap with value at correct place (array[value - 1]) if not the same
        if array[i] != i + 1 and array[i] != array[array[i] - 1]:
            temp = array[i]
            array[i] = array[temp - 1]
            array[temp - 1] = temp
        # else, skip (increment i)
        else:
            i += 1

    # loop sorted array
    for i in range(len(array)):
        # if value != index + 1, add to result
        if array[i] != i + 1:
            return [array[i], i + 1]

    # return result  
    return [-1, -1]

print(findCorruptPair([3, 1, 2, 5, 2])) # [2, 4]
print(findCorruptPair([3, 1, 2, 3, 6, 4])) # [3, 5]