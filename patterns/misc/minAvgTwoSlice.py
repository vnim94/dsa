def minAvgSlice(A):
    # if length < 2, return 0

    # initial min = (A[0] + A[1]) // 2
    min = (A[0] + A[1]) // 2
    start = 0
    # iterate A from index 2 onwards and compare slices of 2 and 3
    for i in range(2, len(A)):
        avg1 = (A[i-1] + A[i]) / 2
        avg2 = (A[i-2] + A[i-1] + A[i]) / 3
        # if 2-slice avg < min, set as min and set start
        if avg1 < min:
            min = avg1
            start = i - 1
        # if 3-slice avg < min, set as min and set start
        if avg2 < min:
            min = avg2
            start = i - 2

    # return start
    return start

print(minAvgSlice([4,2,2,5,1,5,8])) # 1
print(minAvgSlice([1,9,3,5,4,7,2])) # 2
print(minAvgSlice([10, 10, -1, 2, 4, -1, 2, -1])) # 5