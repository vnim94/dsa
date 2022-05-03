def merge(intervals):
    # sort intervals by start
    intervals.sort(key=lambda x:x[0])
    i = 1
    # iterate intervals
    while i < len(intervals):
        current = intervals[i - 1]
        prev = intervals[i]
        # if overlap (prevEnd > currentStart), merge
        if current[1] >= prev[0]:
            # merge: [currentStart, max(currentEnd, prevEnd)]
            intervals[i] = [current[0], max(current[1], prev[1])]
            # remove first interval
            del intervals[i - 1]
        else:
            i += 1

    # return intervals
    return intervals

print(merge([[1,4], [2,5], [7,9]])) # [[1,5], [7,9]]
print(merge([[6,7], [2,4], [5,9]])) # [[2,4], [5,9]]
print(merge([[1,4], [2,6], [3,5]])) # [[1,6]]
print(merge([[2,5]])) # [[2, 5]] 