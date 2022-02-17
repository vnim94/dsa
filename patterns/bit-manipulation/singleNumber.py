def singleNumber(array):
    
    # XOR numbers in the array
    a = array[0]
    for i in range(1, len(array)):
        a ^= array[i]

    # return value
    return a

print(singleNumber([2, 2, 1])) # 1
print(singleNumber([4, 1, 2, 1, 2])) # 4
print(singleNumber([1])) # 1