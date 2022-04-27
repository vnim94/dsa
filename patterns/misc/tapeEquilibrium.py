def tapeEquilibrium(A):
    # sum of array
    total = sum(A)
    currentSum = 0
    min = None
    # iterate
    for i in range(len(A) - 1):
        # add value to currentSum
        currentSum += A[i]
        # minus value from total
        total -= A[i]
        # calculate abs diff
        diff = abs(currentSum - total)
        # check against min
        if min == None or diff < min:
            min = diff
    # return min
    return min

print(tapeEquilibrium([3,1,2,4,3])) # 1
print(tapeEquilibrium([-1000,1000])) # 2000