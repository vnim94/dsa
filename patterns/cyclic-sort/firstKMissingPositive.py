def find(A,k):
    i = 0
    # iterate while value out of position
    while i < len(A):
        # if within bounds (positive and < length) and out of position, swap with value in correct position
        if A[i] > 0 and A[i] < len(A) and A[i] != A[A[i]-1]:
            temp = A[i]
            A[i] = A[temp - 1]
            A[temp - 1] = temp
        # else skip
        else:
            i += 1

print(find([3, -1, 4, 5, 5], 3)) # [1, 2, 6]
print(find([2, 3, 4], 3)) # [1, 5, 6]
print(find([-2, -3, 4], 2)) # [1, 2]
print(find([2, 1, 3, 6, 5],2)) # [4, 7]