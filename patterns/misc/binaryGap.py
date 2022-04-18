def binaryGap(N):
    longest = 0
    binary = bin(N)[2:]
    count = 0
    # iterate digits
    for value in binary:
        # increment count if 0
        if value == '0':
            count += 1
        # if 1, set longest
        if value == '1':
            if count > longest:
                longest = count
            count = 0
    return longest

print(binaryGap(9)) # 2
print(binaryGap(529)) # 4
print(binaryGap(20)) # 1
print(binaryGap(15)) # 0
print(binaryGap(1041)) # 5
print(binaryGap(32)) # 0