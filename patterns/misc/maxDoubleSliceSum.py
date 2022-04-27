def maxDoubleSliceSum(A):
    length = len(A)
    if length < 4:
        return 0
    # cumulative sum array from left to right (excluding first and last)
    LR = [0] * length
    sum = 0
    for i in range(1,length-1):
        sum += A[i]
        sum = max(0, sum)
        LR[i] = sum
    # cumulative sum array from right to left (excluding first and last)
    RL = [0] * length
    sum = 0
    for i in range(length - 2, 0, -1):
        sum += A[i]
        sum = max(0, sum)
        RL[i] = sum

    # iterate from 1 to length - 1, check sum of A[i] + A[i+2] against max
    maxSum = 0
    for i in range(1, length - 2):
        maxSum = max(maxSum, LR[i] + RL[i+2])

    # return max
    return maxSum


print(maxDoubleSliceSum([3,2,6,-1,4,5,-1,2])) # 17
print(maxDoubleSliceSum([5,5,5])) # 0