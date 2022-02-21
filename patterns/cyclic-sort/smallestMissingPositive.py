def findSmallestMissingPositive(array):
    i = 0
    # loop until value in correct position
    while i < len(array):
        # if value has a position in the array and it's not in the correct position, swap
        if array[i] > -1 and array[i] < len(array) and array[i] != array[array[i] - 1]:
            temp = array[i]
            array[i] = array[temp - 1]
            array[temp - 1] = temp
        # else, skip       
        else:
            i += 1

    # loop array
    for i in range(len(array)):
        # first index + 1 where value not in correct position is the smallest missing positive
        if array[i] != i + 1:
            return i + 1


print(findSmallestMissingPositive([-3, 1, 5, 4, 2])) # 3
print(findSmallestMissingPositive([3, -2, 0, 1, 2])) # 4
print(findSmallestMissingPositive([3, 2, 5, 1])) # 4
