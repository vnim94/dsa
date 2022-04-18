def countFactors(N):
    count = 0
    i = 1
    # iterate up to N, check squares
    while i * i < N:
        if N % i == 0:
            count += 2
        i += 1

    if i * i == N:
        count += 1
    
    # return count
    return count

print(countFactors(24)) # 8
print(countFactors(15)) # 3