def maxNonOverlappingSegments(A, B):
    length = len(A)
    # only one segment or zero segments
    if length < 2:
        return length
    
    count = 1
    prevEnd = B[0]

    # iterate to length - 1
    for i in range(len(A) - 1):
        currentStart = A[i + 1]
        currentEnd = B[i + 1]
        # if no overlap (currentStart > prevEnd), add to count and set prevEnd to currentEnd
        if currentStart > prevEnd:
            count += 1
            prevEnd = currentEnd

    # return count
    return count

print(maxNonOverlappingSegments([1,3,7,9,9],[5,6,8,9,10])) # 3