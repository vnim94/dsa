def maxSubarray(A):
    sum = 0
    maxSum = None
    # iterate A
    for value in A:    
        # sum = max of value or sum + value
        sum = max(value, sum + value)
        if maxSum == None or sum > maxSum:
            maxSum = sum
    # return sum
    return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubarray([1])) # 1
print(maxSubarray([5,4,-1,7,8])) # 23