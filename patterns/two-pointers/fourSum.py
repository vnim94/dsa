def fourSum(array, target):
    length = len(array)
    result = []
    # sort array
    array.sort()
    # iterate array until 4th last
    for i in range(length - 3):
        # skip duplicates
        if i > 0 and array[i] == array[i-1]:
            continue
        # iterate array beginning from after first pointer up to 3rd last
        for j in range(i+1, length - 2):
            # skip duplicates
            if j > i + 1 and array[j] == array[j-1]:
                continue
            start = j + 1
            end = length - 1
            # use two pointers (start & end), 
            while start < end:
                # if sum of elements = target, append to result
                sum = array[i] + array[j] + array[start] + array[end]
                if sum == target:
                    result.append([array[i],array[j],array[start],array[end]])
                    # increment start and skip duplicates
                    start += 1
                    while start < end and array[start] == array[start - 1]:
                        start += 1
                    # decrement end and skip duplicates
                    end -= 1
                    while start < end and array[end] == array[end + 1]:
                        end -= 1
                # if sum < target, increment start
                elif sum < target:
                    start += 1                        
                # if sum > target, decrement end
                else:
                    end -= 1
    # return result
    return result

print(fourSum([4,1,2,-1,1,-3], 1)) # [-3,-1,1,4], [-3,1,1,2]
print(fourSum([2,0,-1,1,-2,2], 2)) # [-2,0,2,2], [-1,0,1,2]
print(fourSum([1,0,-1,0,-2,2], 0)) # [-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]
print(fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)) # [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]]