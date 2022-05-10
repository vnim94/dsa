def triangle(A):
    # sort
    A.sort()
    # iterate and return true if X + Y > Z satisfied (other conditions will satisfied as sorted)
    for i in range(len(A) - 2):
        if A[i] + A[i+1] > A[i+2]: 
            return True
    # return false
    return False

print(triangle([10,2,5,1,8,20])) # true
print(triangle([10,50,5,1])) # false