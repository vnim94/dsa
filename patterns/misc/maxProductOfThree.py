def maxProductOfThree(array):
    # sort array
    array.sort()
    length = len(array)
    # either 2 negatives * largest positive or largest positives
    negatives = array[0] * array[1] * array[length - 1]
    positives = array[length - 1] * array[length - 2] * array[length - 3]

    return max(negatives, positives)

print(maxProductOfThree([-3,1,2,-2,5,6])) # 60