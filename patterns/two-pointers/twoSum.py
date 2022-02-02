def twoSum(array, target):
    # initialise start and end pointers
    start = 0
    end = len(array) - 1
    # increment start / decrement end depending on if sum < / > target
    while start < end:
        sum = array[start] + array[end]

        # return [start, end] if sum = target
        if sum == target:
            return [start, end]

        # if sum < target, need larger numbers -> increment start
        if sum < target:
            start += 1
        # if sum > target, need smaller numbers -> decrement end
        else:
            end -=1

    # else return 0
    return 0

print(twoSum([1, 2, 3, 4, 6], 6)) # [1,3]
print(twoSum([2, 5, 9, 11], 11)) # [0,2]