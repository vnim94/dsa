def sort(A):
    low = 0
    high = len(A) - 1
    i = 0
    # iterate through A while < high pointer
    while i <= high: 
        # if A[i] = 0, swap with low pointer
        if A[i] == 0:
            A[i], A[low] = A[low], A[i]
            low += 1
        # if A[i] = 2, swap with high pointer
        elif A[i] == 2:
            A[i], A[high] = A[high], A[i]
            high -= 1
        
        i += 1
        
    return A

print(sort([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(sort([2,0,1])) # -> [1,0,2] -> [0,1,2]