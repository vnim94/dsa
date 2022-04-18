def pairs(A, k):
    # sort A
    A.sort()
    count = 0
    start = 0
    end = 1
    # iterate while b < length
    while end < len(A):    
        diff = A[end] - A[start]
        # if diff = k, increment count and b
        if diff == k:
            count += 1
            end += 1
        # if diff > k, need smaller diff -> increment a
        elif diff > k:
            start += 1
        # if diff < k, need larger diff -> increment b
        elif diff < k:
            end += 1

    # return count
    return count

print(pairs([1,2,3,4], 1)) # 3
print(pairs([1,5,3,4,2], 2)) # 3
