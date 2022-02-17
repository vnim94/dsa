def findMissingNumber(array):
    n = len(array) + 1
    # XOR numbers in the array 
    a = array[0]
    for i in range(1, n - 1):
        a ^= array[i]
    # XOR numbers in range
    b = 1
    for i in range(2, n + 1):
        b ^= i
    # return XOR of both results
    return a ^ b

print(findMissingNumber([1,5,2,6,4])) # 3
print(findMissingNumber([1,5,6,3,4,8,7])) # 2
