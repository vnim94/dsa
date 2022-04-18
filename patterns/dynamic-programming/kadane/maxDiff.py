def maxDiff(A):
    maxValue = None
    maxDiff = None
    for i in range(len(A) - 1, -1, -1):
        if maxValue == None or A[i] > maxValue:
            maxValue = A[i]
        if A[i] < maxValue:
            diff = maxValue - A[i]
            if maxDiff == None or diff > maxDiff:
                maxDiff = diff

    if maxDiff == None:
        return -1
    return maxDiff
    
def maxDiff(A):
    minimum = None
    maxDiff = None

    for i in range(len(A)):
        if minimum == None or A[i] < minimum:
            minimum = A[i]

        if A[i] > minimum:
            diff = A[i] - minimum
            if maxDiff == None or diff > maxDiff:
                maxDiff = diff

    if maxDiff == None:
        return -1
    return maxDiff


print(maxDiff([7,1,5,4])) # 4
print(maxDiff([9,4,3,2])) # -1
print(maxDiff([1,5,2,10])) # 9
