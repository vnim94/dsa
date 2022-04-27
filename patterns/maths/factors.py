def countFactors(N):
    count = 0
    i = 1
    # iterate up to N, check squares
    while i * i < N:
        # if divisible, is a factor 
        if N % i == 0:
            # increment count to include value and its square
            count += 2
        i += 1

    # include perfect square
    if i * i == N:
        count += 1
    
    # return count
    return count

print(countFactors(24)) # 8
print(countFactors(15)) # 3