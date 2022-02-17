def findDistinctSubsets(array):
    # sort the array
    array.sort()
    # create empty subsets
    subsets = [[]]
    # loop array
    for v in range(len(array)):
        length = len(subsets)
        i = 0
        # if current = prev, increment iteration by 2^v
        if v > 0 and array[v] == array[v - 1]:
            i += 2**(v-1)
        # loop subsets
        while i < length: 
            subsets.append(subsets[i] + [array[v]])
            i += 1

    # return subsets
    return subsets

print(findDistinctSubsets([3, 1, 3, 5])) # [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]