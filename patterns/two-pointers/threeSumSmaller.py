def threeSumSmaller(array, target):
    # sort array
    array.sort()
    count = 0
    # iterate array
    for i in range(len(array)):
        # using two start and end pointers, 
        start = i + 1
        end = len(array) - 1
        while start < end:
            sum = array[i] + array[start] + array[end]
            # if current + pair < target, add to result
            if sum < target:
                count += end - start # everything before end if smaller, there just add diff between end and start
                start += 1
            end -= 1

    # return count
    return count

print(threeSumSmaller([-1, 0, 2, 3], 3)) # 2, [-1, 0, 3], [-1, 0, 2]
print(threeSumSmaller([-1, 4, 2, 1, 3], 5)) # 4, [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
print(threeSumSmaller([-2,0,1,3], 2)) # 2, [-2,0,1], [-2,0,3]
print(threeSumSmaller([], 0)) # 0
print(threeSumSmaller([0], 0)) # 0