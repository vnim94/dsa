# in place
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

# using hash table
def findSmallestMissingPositive(array):
    nums = {}
    length = len(array)
    # iterate array and store positive values in hash table
    for value in array:
        if value > 0:
            nums[value] = 1
    # iterate from 1 onwards (inclusive)
    for i in range(1, length + 1):    
        # if not in hash table, return it
        if i not in nums:
            return i
    # if all numbers positive, return next
    return length + 1

print(findSmallestMissingPositive([-3, 1, 5, 4, 2])) # 3
print(findSmallestMissingPositive([3, -2, 0, 1, 2])) # 4
print(findSmallestMissingPositive([3, 2, 5, 1])) # 4
print(findSmallestMissingPositive([2,-1,-1,-1,-1])) # 1
