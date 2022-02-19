def findPermutationsRecursively(array):
    
    # base case: array length = 1 -> return [array]
    if len(array) == 1:
        return [array]

    # result array
    results = []

    # loop array
    for value in array:
        copy = array.copy()
        copy.remove(value)
        # recursively call with array without current value
        perms = findPermutationsRecursively(copy)
        # loop returned result
        for i in range(len(perms)):
            # insert value 
            perms[i].insert(i, value)
        # add to results
        results += perms

    # return results
    return results

print(findPermutationsRecursively([1])) # [[1]]
print(findPermutationsRecursively([0, 1])) # [[0,1],[1,0]]
print(findPermutationsRecursively([1, 2, 3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def findPermutationsIteratively(array):
    None
    # results array

    # loop values

        # 


print(findPermutationsIteratively([1])) # [[1]]
print(findPermutationsIteratively([0, 1])) # [[0,1],[1,0]]
print(findPermutationsIteratively([1, 2, 3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]