def rotateRight(array, n):
    # edge case: length = 0 -> return array
    length = len(array)
    if length == 0:
        return array
    
    output = [0] * length

    # reduce n to lowest common multiple
    n = n % length
    index = 0
    # iterate array starting from length - n onwards
    for i in range(length - n, length):
        output[index] = array[i]
        index += 1

    # iterate array until length - n (exclusive)
    for i in range(length - n):
        output[index] = array[i]
        index += 1

    return output

def rotateRightInPlace(array,n):
    length = len(array)
    # reverse array
    reverse(array, 0, length - 1)

    # reverse up to n
    reverse(array, 0, n - 1)

    # reverse from n onwards
    reverse(array, n, length - 1)
    
    # return array
    return array

def reverse(array, start, end):
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    
def rotateLeft(array, n):
    length = len(array)
    # if empty, return array
    if length == 0:
        return array
    # create output 
    output = [0] * length
    # resolve n
    n = n % length
    index = 0
    # iterate from n onwards
    for i in range(n, length):
        output[index] = array[i]
        index += 1
    # iterate up to n
    for i in range(n):
        output[index] = array[i]
        index += 1

    # return output
    return output


print(rotateRight([], 1), rotateLeft([], 1)) # []
print(rotateRight([1], 3), rotateLeft([1], 3)) # [1]
print(rotateRight([1,2], 3), rotateLeft([1,2], 3)) # [1]
print(rotateRight([0, 0, 0], 1), rotateLeft([0, 0, 0], 1)) # [0, 0, 0]
print(rotateRight([1, 2, 3, 4], 4), rotateLeft([1, 2, 3, 4], 4)) # [1, 2, 3, 4]
print(rotateRight([3, 8, 9, 7, 6], 3), rotateLeft([3, 8, 9, 7, 6], 3)) # [9, 7, 6, 3, 8] [7, 6, 3, 8, 9]