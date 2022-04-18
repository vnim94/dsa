def minDiff(array):
    a = sum(array)
    b = 0
    m = None
    for i in range(len(array)-1):
        b += array[i]
        a -= array[i]
        d = abs(a - b)
        if m == None or d < m:
            m = d
    
    return m

print(minDiff([3,1,2,4,3])) # 1