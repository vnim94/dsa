def quickSort(array, start, end):

    # if start >= end -> return
    if start >= end:
        return
    # partition the array
    index = partition(array, start, end)
    
    # quickSort left
    quickSort(array, start, index - 1)

    # quickSort right
    quickSort(array, index + 1, end)

    # return array     
    return array

def partition(array, start, end):
    # set pivot
    pivot = array[end]
    pointer = start

    # move values < pivot to left of array
    for i in range(start, end):
        # if value < pivot, swap with value at pointer
        if array[i] < pivot:
            temp = array[pointer]
            array[pointer] = array[i]
            array[i] = temp

            pointer += 1

    # swap pivot with pointer
    temp = array[pointer]
    array[pointer] = array[end]
    array[end] = temp

    return pointer

array = [3, 5, 4, 6, 2, 1]

print(quickSort(array, 0, len(array) - 1))