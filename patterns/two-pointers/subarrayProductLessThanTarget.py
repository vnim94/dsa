def productLessThanTarget(array, target):
    start = 0
    product = 1
    result = []
    # iterate array
    for end in range(len(array)):
        # multiply current product by current value
        product *= array[end]
        # while product >= target and start < length, divide by start and increment start
        while product >= target and start < len(array):
            product /= array[start]
            start += 1

        # add each separate element in subarray to result (excluding start)
        for i in range(start + 1, end + 1):
            result.append([array[i]])

        # add subarray to result
        result.append(array[start:end+1])

    # return result
    return result

print(productLessThanTarget([2, 5, 3, 10], 30)) # [2], [5], [2, 5], [3], [5, 3], [10] 
print(productLessThanTarget([8, 2, 6, 5], 50)) # [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
print(productLessThanTarget([10, 5, 2, 6], 100)) # [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].