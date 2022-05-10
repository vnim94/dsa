# brute force
def minAbsSumOfTwo(A):
    min = None
    length = len(A)

    if length < 2:
        return 0

    # iterate A
    for i in range(length):
        # iterate from i + 1 onwards
        for j in range(i+1,length):
            # check abs sum against min
            absSum = abs(A[i]+A[j])
            if min == None or absSum < min:
                min = absSum
    # return min
    return min

# efficient
def minAbsSumOfTwo(A):
    length = len(A)
    # sort A
    A.sort()
    start = 0
    end = length - 1
    minAbsSum = None
    # iterate while start <= end
    while start <= end:
        sum = A[start] + A[end]
        # take min of currentMin vs abs(A[start] + A[end])
        if minAbsSum == None or abs(sum) < minAbsSum:
            minAbsSum = abs(sum)
        # if A[start] + A[end] < 0, need larger number to get to 0, increment start
        if sum <= 0:
            start += 1
        # else, need smaller number to get to 0, decrement end
        else:
            end -= 1

    # return min
    return minAbsSum

print(minAbsSumOfTwo([1,4,-3])) # 1 -> [-3,1,4]
print(minAbsSumOfTwo([-8,4,5,-10,3])) # 3  -> [-10,-8,3,4,5]
print(minAbsSumOfTwo([1000000000])) # 2000000000