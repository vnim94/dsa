def largestSubarray(array, k):
    # initialise start of window
    start = 0
    largest = None
    # increment end of window
    for end in range(len(array)):
        # if criteria met
        if end - start == k - 1:
            # if value of index > value of max index, set max as index
            if largest == None or array[start] > array[largest]:
                largest = start
            # slide window
            start += 1

    # return array[index:index+k]
    return array[largest:largest + k]

print(largestSubarray([1,4,5,2,3], 3)) # [5,2,3]
print(largestSubarray([1,4,5,2,3], 4)) # [4,5,2,3]
print(largestSubarray([1,4,5,2,3], 1)) # [5] 