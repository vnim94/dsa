def countDistinct(A):
    # sort
    A.sort()
    count = 1
    # iterate A
    for i in range(1, len(A)):
        # if current value != previous, add to count
        if A[i] != A[i-1]:
            count += 1
    # return count
    return count

print(countDistinct([2, 1, 1, 2, 3, 1])) # 3
print(countDistinct([2, 3, 3, 3, 6, 9, 9])) # 4
print(countDistinct([2, 2, 2, 11])) # 2