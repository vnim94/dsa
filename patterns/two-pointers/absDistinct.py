def absDistinct(A):
    back = 0
    front = len(A) - 1
    count = 0
    current = None
    former = None
    # iterate while back < front
    while back < front:
        # if front >= back, current = |A[front]| decrement front,
        if abs(A[back]) <= abs(A[front]):
            current = abs(A[front])
            front -= 1
        # else, current = |A[back]|, increment back
        else:
            current = abs(A[back])
            back -= 1
        # if current != former, add to distinct count
        print(current, former)
        if current != former:
            count += 1
        # set former to current
        former = current

    # return count
    return count

def absDistinctInPlace(A):
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