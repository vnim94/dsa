def search(array, target):

    # check if asc or desc
    desc = False
    if array[0] > array[len(array) - 1]:
        desc = True

    # set start and end
    start = 0
    end = len(array) - 1

    # loop until start > end
    while start <= end:
        # set mid (start + end // 2)
        mid = (start + end) // 2
        
        # if array[mid] = target, return mid
        if array[mid] == target:
            return mid
        # if array[mid] < target, search right (start = mid + 1)
        elif array[mid] < target:
            if desc:
                end = mid - 1
            else:
                start = mid + 1
        # if array[mid] > target, search left (end = mid - 1)
        elif array[mid] > target:
            if desc:
                start = mid + 1
            else:
                end = mid - 1
            

    # return -1 if not found
    return -1

print(search([4, 6, 10], 10)) # 2
print(search([1, 2, 3, 4, 5, 6, 7], 5)) # 4
print(search([10, 6, 4], 10)) # 0
print(search([10, 6, 4], 4)) # 2