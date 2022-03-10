def threeSum(array):
    # sort array
    array.sort()
    result = []
    # iterate array
    for i in range(len(array)):
        # skip duplicate
        if i > 0 and array[i] == array[i - 1]:
            continue
        # target is -current value
        target = -array[i]
        start = i + 1
        end = len(array) - 1
        # use two pointers to find pair where sum = target
        while start < end:
            sum = array[start] + array[end]
            # if sum = target, add to result
            if sum == target:
                result.append([-target, array[start], array[end]])
                start +=1
                end -=1
                # if new start same as prev, skip. start must < end
                while start < end and array[start] == array[start - 1]:
                    start += 1
                # if new end same as prev skip
                while end > start and array[end] == array[end + 1]:
                    end -= 1
            # if sum < target, increment start
            elif sum < target:
                start += 1
            # if sum > target, decrement end
            else:
                end -= 1

    # return result
    return result
# [-3,-2,-1,0,1,1,2]
print(threeSum([-3, 0, 1, 2,-1, 1, -2])) # [[-3,1,2], [-2,0,2], [-2,1,1], [-1,0,1]]
print(threeSum([-5, 2, -1, -2, 3])) # [[-5,2,3], [-2,-1,3]]
print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([-2,0,0,2,2])) # [[-2,0,2]]