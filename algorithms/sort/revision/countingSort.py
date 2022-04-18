def countingSort(array):
    # create count array based on max + 1
    count = [0] * (max(array) + 1)
    # fill count array
    for i in range(len(array)):
        count[array[i]] += 1
    # update count array with cumulative sum
    for i in range(len(count) - 1):
        count[i+1] += count[i]
    
    # shift count array to right
    for i in range(len(count) - 1, 0, -1):
        count[i] = count[i-1]
    # create output array
    output = [0] * len(array)
    # iterate array and fill output array using count array values as indices
    for i in range(len(array)):
        output[count[array[i]]] = array[i]
        count[array[i]] += 1

    # return array
    return output

array = [1,0,3,1,3,1]
print(countingSort(array))