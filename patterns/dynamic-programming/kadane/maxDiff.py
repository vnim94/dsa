def maxDiff(A):
    min = None
    maxDiff = None
    # iterate A
    for value in A:
        # record min
        if min == None or value < min:
            min = value
        # if value > min, calculate diff
        if value > min:
            diff = value - min
            # check against maxDiff
            if maxDiff == None or diff > maxDiff:
                maxDiff = diff

    # return maxDiff, else -1 if no maxDiff
    if maxDiff == None:
        return -1
    return maxDiff

print(maxDiff([7,1,5,4])) # 4
print(maxDiff([9,4,3,2])) # -1
print(maxDiff([1,5,2,10])) # 9
