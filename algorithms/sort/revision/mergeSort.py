def mergeSort(array):
    # if single value, return it
    if len(array) == 1:
        return array
    # get mid
    mid = len(array) // 2

    # sort left
    left = array[:mid]
    mergeSort(left)

    # sort right
    right = array[mid:]
    mergeSort(right)

    # merge sorted left and right
    merge(left, right, array)

def merge(left, right, array):
    l = 0
    r = 0
    a = 0

    # place elements in array
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[a] = left[l]
            l += 1
        else:
            array[a] = right[r]
            r += 1
        a +=1

    while l < len(left):
        array[a] = left[l]
        l += 1
        a += 1

    while r < len(right):
        array[a] = right[r]
        r += 1
        a += 1

array = [7,5,9,3,8,4,6,2,1]
mergeSort(array)
print(array)