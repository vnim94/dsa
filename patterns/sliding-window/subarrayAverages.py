def findSubarrayAverages(array, size):

    # initialise start of window and averages array
    start = 0
    averages = []
    sum = 0
    # increment end of window 
    for end in range(len(array)):
        # add to sum 
        sum += array[end]
        # if criteria met (size = 5), 
        if end + 1 - start == size:
            # calculate average 
            average = sum / size
            # add to results array
            averages.append(average)
            # reduce sum 
            sum -= array[start]
            # increment start of window
            start += 1

    # return averages
    return averages

print(findSubarrayAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)) # [2.2, 2.8, 2.4, 3.6, 2.8]