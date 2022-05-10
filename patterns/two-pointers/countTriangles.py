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
            # add number of triangles between Z and Y
            diff = (Z - 1) - Y
            count += diff

    # return count
    return count

print(countTriangles([10,2,5,1,8,12])) # 4 [1,2,5,8,10,12] -> (5,8,10), (5,8,12), (5,10,12), (8,10,12)
# print(countTriangles([3,3,5,6])) # 3 -> (3,3,5) (3,3,6) (3,5,6)