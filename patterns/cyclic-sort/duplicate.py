def findDuplicate(array):

    i = 0
    while i < len(array):
        # if value not in correct position
        if array[i] - 1 != i:
            # if value equal to value at correct position, duplicate found
            if array[i] == array[array[i] - 1]:
                return array[i]
            # else, swap
            temp = array[i]
            array[i] = array[temp - 1]
            array[temp - 1] = temp
        # else skip
        else:
            i += 1

print(findDuplicate([1, 4, 4, 3, 2])) # 4
print(findDuplicate([2, 1, 3, 3, 5, 4])) # 3
print(findDuplicate([2, 4, 1, 4, 4])) # 4