def squareArray(array):
    
    # initialise output array and start & end pointers  
    output = [None] * len(array)
    start = 0 
    end = len(array) - 1
    index = end

    # loop through array
    while start <= end:
        squaredStart = array[start] ** 2
        squaredEnd = array[end] ** 2
        # store greater value at end of output, increment start / decrement end, decrement index
        if squaredStart > squaredEnd:
            output[index] = squaredStart
            start += 1
        else:
            output[index] = squaredEnd
            end -= 1
        
        index -= 1

    # return output
    return output

print(squareArray([-2, -1, 0, 2, 3])) # [0, 1, 4, 4, 9]
print(squareArray([-3, -1, 0, 1, 2])) # [0, 1, 1, 4, 9]