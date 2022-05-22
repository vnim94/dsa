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

def maxSubarray(A):
    # create table of solutions
    s = [0] * len(A)
    # seed table
    s[0] = A[0]

    maxSum = s[0]
    # iterate table
    for i in range(1, len(A)):
        if s[i-1] > 0:
            s[i] = A[i] + s[i-1]
        else:
            s[i] = A[i]
        maxSum = max(maxSum, s[i])
    # return max
    return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubarray([1])) # 1
print(maxSubarray([5,4,-1,7,8])) # 23
print(maxSubarray([3,2,-6,4,0])) # [3,2] -> 5
print(maxSubarray([5,-7,3,5,-2,4,-1])) # [3,5,-2,4] -> 10
print(maxSubarray([-2,1])) # 1