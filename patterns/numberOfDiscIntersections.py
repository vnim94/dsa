def count(A):
    length = len(A)
    # create arrays of start and end points
    start = [i - A[i] for i in range(length)]
    end = [i + A[i] for i in range(length)]
    # sort the arrays
    start.sort()
    end.sort()
    # iterate length of A
    j = 0
    count = 0
    for i in range(length):
        # iterate end and count where end >= start
        while j < length and end[i] >= start[j]:
            count += j - i

            if count > 10000000:
                return -1

            j += 1

    # return count
    return count

print(count([1,5,2,1,4,0])) # 11