def tie(K, A):
    length = 0
    count = 0
    # iterate A
    for value in A:
        # add value to length
        length += value
        # if length >= K, increment count and reset length to 0
        if length >= K:
            count += 1
            length = 0

    # return count
    return count

print(tie(4, [1,2,3,4,1,1,3])) # 3