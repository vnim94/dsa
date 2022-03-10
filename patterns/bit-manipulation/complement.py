def complement(num):
    count = 0
    n = num
    # number of bits
    while n > 0:
        n = n >> 1
        count += 1

    # if only 1 bit, return xor of 1
    if count == 0:
        return num ^ 1

    # bit set = 2^bits - 1
    bitSet = 2 ** count - 1
    
    # return num ^ bit set
    return num ^ bitSet

print(complement(0)) # 1
print(complement(1)) # 0
print(complement(8)) # 7
print(complement(10)) # 5