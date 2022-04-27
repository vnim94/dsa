def absDistinct(A):
    count = len(A)
    start = 0
    end = count - 1
    
    # iterate using two pointers (start & end)
    while start < end:    
        # skip equal adjacent values
        while start < end and A[start] == A[start+1]:
            start += 1
            count -= 1
        while start < end and A[end] == A[end-1]:
            end -= 1
            count -= 1
        
        # if start = end, break out of loop
        if start == end:
            break
        
        # if sum of two pointers is 0, not distinct
        if A[start] + A[end] == 0:
            count -= 1
            start += 1
            end -= 1
        # if negative sum, move right to check for any additional 0-sums
        elif A[start] + A[end] < 0:
            start += 1
        # if positive sum, move left to check for any additional 0-sum
        elif A[start] + A[end] > 0:
            end -= 1

    # return count
    return count

print(absDistinct([-5,-3,-1,0,3,6])) # 5
print(absDistinct([1,1]))