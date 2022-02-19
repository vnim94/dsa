def sort(array):
    # loop array
    for i in range(1, len(array)):
        # if current < previous, swap until not < previous
        current = i
        while current > 0 and array[current] < array[current - 1]:
            temp = array[current]
            array[current] = array[current - 1]
            array[current - 1] = temp

            current -= 1

    # return array
    return array

print(sort([5,3,6,2,7,4,1]))