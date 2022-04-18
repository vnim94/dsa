def triangle(A):
    # sort
    A.sort()
    # iterate and return true if conditions satisfied
    for i in range(len(A) - 2):
        if A[i] + A[i+1] > A[i+2] and A[i] + A[i+2] > A[i+1] and A[i+1] + A[i+2] > A[i]:
            return True
    # return false
    return False

print(triangle([10,2,5,1,8,20])) # true
print(triangle([10,50,5,1])) # false