def threeSumClose(array, target):
    # sort array
    array.sort()
    closest = None
    # iterate array
    for i in range(len(array)):
        # use two pointers to find pair
        start = i + 1
        end = len(array) - 1
        while start < end:
            sum = array[i] + array[start] + array[end]
            diff = target - sum
            # if diff = 0, return it
            if diff == 0:
                return sum

            # if closest is None or abs(target - pair sum) < abs(target - closest), set as closest
            if closest == None or abs(diff) < abs(target - closest):
                closest = sum

            # if diff > 0, larger triplet needed -> increment start, else decrement end
            if diff > 0:
                start += 1
            else:
                end -= 1

    # return closest
    return closest

print(threeSumClose([-1,2,1,-4],1)) # 2
print(threeSumClose([0,0,0],1)) # 0
print(threeSumClose([0,2,1,-3], 1)) # 0