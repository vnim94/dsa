def countDivisor(N):
    count = 0
    i = 1
    while i * i < N:
        if N % i == 0:
            count += 2
        i += 1

    # perfect square
    if i * i == N:
        count += 1

    return count

print(countDivisor(36)) # 9
print(countDivisor(24)) # 7 
print(countDivisor(12)) # 5