def findSubsets(array):
    # create empty set
    subsets = [[]]
    # loop array
    for value in array:
        length = len(subsets)
        # loop through existing subsets 
        for i in range(length):
            # add new subset based on existing subset + value
            subsets.append(subsets[i] + [value])

    # return set
    return subsets

print(findSubsets([0])) # [[], [0]]
print(findSubsets([1, 2, 3])) # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]] 