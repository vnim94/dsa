def maxAverageSubarray(array, k):
    
    start = 0
    max = 0
    sum = 0

    # increase window size until criteria met (size = k)
    for end in range(len(array)):
        sum += array[end]
        # record average if > max
        if end >= k - 1:
            if sum / k > max:
                max = sum / k
            # slide window
            sum -= array[start]
            start += 1

    # return max
    return max

print(maxAverageSubarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)) # [2.2, 2.8, 2.4, 3.6, 2.8] -> 3.6