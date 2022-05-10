def findMissingNumber(array):
    length = len(array)
    # XOR array
    a = 0
    for i in range(length):
        a ^= array[i]
    # XOR range
    b = 0
    for i in range(1, length + 2): # including n (1 to n + 1)
        b ^= i

    # return XOR of both
    return a ^ b

print(findMissingNumber([1,5,2,6,4])) # 3
print(findMissingNumber([1,5,6,3,4,8,7])) # 2
