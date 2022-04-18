def countDistinctSlices(M, A):
    # initialise start, end and count
    start = 0
    end = 0
    seen = {}
    count = 0
    length = len(A)
    # iterate while start and end < length
    while start < length and end < length:
        # if end already seen, reset, increment start and set end as start
        if A[end] in seen:
            seen = {}
            start += 1
            end = start
        # else add to count and seen, increment end 
        else:
            count += 1
            seen[A[end]] = True
            if end + 1 == length:
                end = start
            else:
                end += 1
        
    # return count
    return count
    
def countDistinctSlices(M, A):
    start = 0
    end = 0
    length = len(A)
    seen = {}
    count = 0
    # iterate while start < length
    while start < length:
        # iterate while end < length and not seen
        while end < length and A[end] not in seen:    
            # add value to seen
            seen[A[end]] = True
            # increment end
            end += 1
        # increment count by end - start
        count += end - start
        # return if > 1,000,000,000
        if count > 1000000000:
            return 1000000000

        # increment start
        if start <= end and start < length:
            del seen[A[start]]
            start += 1

    # return count
    return count

print(countDistinctSlices(6,[3,4,5,5,2])) # 9
print(countDistinctSlices(5,[2,3,3,6,7])) # 9