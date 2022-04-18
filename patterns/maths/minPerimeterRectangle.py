def findMinPerimeter(N):
    # find smallest sum of factors
    i = 1
    min = None
    while i * i <= N:
        if N % i == 0:
            perimeter = 2 * (i + N // i)
            if min == None or perimeter < min:
                min = perimeter

        i += 1
    
    return min

print(findMinPerimeter(30)) # 22