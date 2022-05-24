def dominator(A):
    counts = {}
    index = 0
    # iterate A
    for value in A:
        # add value to hashmap
        counts[value] = counts.get(value, 0) + 1
        # if count > length // 2, return index
        if counts[value] > len(A) // 2:
            return index
        # increment index
        index += 1

    # return -1
    return -1

print(dominator([3,4,3,2,3,-1,3,3])) # 0 / 2 / 4 / 6 / 7
print(dominator([])) # -1