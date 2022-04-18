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
    
def rotate(A, k):
    length = len(A)
    output = [0] * length

    # iterate A
    for i in range(length):
        # calculate final position
        index = (i + k) % length
        # assign to output
        output[index] = A[i]

    # return output
    return output

def rotateLeft(A, k):
    length = len(A)
    output = [0] * length
    
    for i in range(length):
        index = i - (k % length)
        if index < 0:
            index += length

        output[index] = A[i]

    return output

print(rotate([], 1), rotateLeft([], 1)) # []
print(rotate([1], 3), rotateLeft([1], 3)) # [1]
print(rotate([1,2], 3), rotateLeft([1,2], 3)) # [1]
print(rotate([0, 0, 0], 1), rotateLeft([0, 0, 0], 1)) # [0, 0, 0]
print(rotate([1, 2, 3, 4], 4), rotateLeft([1, 2, 3, 4], 4)) # [1, 2, 3, 4]
print(rotate([3, 8, 9, 7, 6], 3), rotateLeft([3, 8, 9, 7, 6], 3)) # [9, 7, 6, 3, 8] [7, 6, 3, 8, 9]