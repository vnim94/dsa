# def cyclicSort(array):
#     i = 0
#     # loop in same spot until correct value in place
#     while i < len(array):
#         # if value in wrong place (i.e not equal index), swap with value in correct place
#         if array[i] - 1 != i:
#             temp = array[i]
#             array[i] = array[temp - 1]
#             array[temp - 1] = temp
#         else:
#             i += 1

#     # return array
#     return array

def cyclicSort(array):
    i = 0
    # iterate until value in correct position
    while i < len(array):
        # if value out of position, put into correct position
        if array[i] - 1 != i:
            index = array[i] - 1
            array[i], array[index] = array[index], array[i]
        # else, skip
        else:
            i += 1

    # return array
    return array

print(cyclicSort([3, 1, 5, 4, 2]))
# print(cyclicSort ([2, 6, 4, 3, 1, 5]))
# print(cyclicSort ([1, 5, 6, 4, 3, 2]))