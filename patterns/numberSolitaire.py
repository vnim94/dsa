def numberSolitaire(A):
    # base case: if length = 1 -> return value
    if len(A) == 1:
        return A[0]
    
    total = A[0]
    max = 0

    # iterate options
    for i in range(1,7):
        # recurse with A[i:] and add result to sum
        if i < len(A):
            total += numberSolitaire(A[i:])
            # set max
            if total > max:
                max = total

    # return max
    return max

print(numberSolitaire([1])) # 1
print(numberSolitaire([1,-2,0,9,-1,-2])) # 8