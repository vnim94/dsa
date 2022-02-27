def merge(intervals):
    # sort intervals by start
    intervals.sort(key=lambda x:x[0])
    i = 1
    # iterate intervals
    while i < len(intervals):
        A = intervals[i - 1]
        B = intervals[i]
        # if overlap (endA > startB), merge
        if A[1] > B[0]:
            # merge: [startA, max(endA, endB)]
            intervals[i] = [A[0], max(A[1], B[1])]
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