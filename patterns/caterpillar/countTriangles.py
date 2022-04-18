def countTriangles(A):
    # sort A
    A.sort()
    
    count = 0
    length = len(A)
    
    # iterate A (X)
    for X in range(length):
        Z = X + 2
        # iterate from X + 1 (Y)
        for Y in range(X + 1, length):
            # iterate while X + 2 (Z) < length and triangle condition satisfied
            while Z < length and A[X] + A[Y] > A[Z]:
                Z += 1
            # add Z - Y - 1
            diff = Z - Y - 1
            count += diff

    # return count
    return count


print(countTriangles([10,2,5,1,8,12])) # 4