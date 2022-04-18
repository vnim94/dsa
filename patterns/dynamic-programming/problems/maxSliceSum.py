def maxSliceSum(A):
    maxSum = None
    sum = 0
    # iterate A
    for value in A:
        # set sum as larger of current sum + value or value
        if sum + value > value:
            sum = sum + value
        else:
            sum = value
        # check maxSum
        if maxSum == None or sum > maxSum:
            maxSum = sum

    # return maxSum
    return maxSum

print(maxSliceSum([3,2,-6,4,0])) # [3,2] -> 5
print(maxSliceSum([5,-7,3,5,-2,4,-1])) # [3,5,-2,4] -> 10