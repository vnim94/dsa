def smallestSubarrayWithGivenSum(array, s):

    start = 0
    sum = 0
    min = len(array) + 1

    # add to sum until >= s
    for end in range(len(array)):
        sum += array[end]

        # while sum >= s, check length and shrink
        while sum >= s:
            # check if smaller than min
            length = end - start + 1
            if length < min:
                min = length

            # shift window
            sum -= array[start]
            start += 1
            
    # return min or 0 if not possible
    if min == len(array) + 1:
        return 0
    return min
    
    
print(smallestSubarrayWithGivenSum([2, 1, 5, 2, 3, 2], 7)) # 2
print(smallestSubarrayWithGivenSum([2, 1, 5, 2, 8], 7)) # 1
print(smallestSubarrayWithGivenSum([3, 4, 1, 1, 6], 8)) # 3