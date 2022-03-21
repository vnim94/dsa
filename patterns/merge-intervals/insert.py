def insert(intervals, new):
    
    result = []
    length = len(intervals)
    i = 0
    # find index to insert new (i.e where current[end] < new[start])
    while i < length and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # merge new with overlapping intervals 
    while i < length and intervals[i][0] <= new[1]:
        new[0] = min(intervals[i][0], new[0])
        new[1] = max(intervals[i][1], new[1])
        i += 1

    # insert new
    result.append(new)

    # add remaining non-overlapping intervals
    while i < length:
        result.append(intervals[i])
        i += 1

    # return intervals
    return result

print(insert([],[1,5])) # [[1,5]]
print(insert([[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]] 
print(insert([[1,5]], [2,7])) # [[1,7]]
print(insert([[1,5]], [2,3])) # [[1,5]]