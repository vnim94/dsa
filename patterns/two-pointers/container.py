def maxArea(height):
    maximum = 0
    start = 0
    end = len(height) - 1
    # iterate while start < end
    while start < end:
        # take min of height[start] and height[end]
        minHeight = min(height[start], height[end])
        # check end + 1 - start * min against max
        maximum = max(maximum, (end - start) * minHeight)
        # increment / decrement start / end based on smaller
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    # return max
    return maximum

print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1