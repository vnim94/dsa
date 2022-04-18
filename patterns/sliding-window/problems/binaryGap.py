def binaryGap(num):
    binary = bin(num)
    # initialise start and longest 
    start = 2
    longest = 0
    # increment end 
    for end in range(3,len(binary)):
        # if start and end = 1
        if binary[start] == '1' and binary[end] == '1':
            gap = end - (start + 1)
            # record longest
            if gap > longest:
                longest = gap
            # set start as end
            start = end

    # return longest
    return longest

print(binaryGap(9)) # 2
print(binaryGap(529)) # 4
print(binaryGap(20)) # 1
print(binaryGap(15)) # 0
print(binaryGap(32)) # 0
print(binaryGap(1042)) # 5

# time complexity: O(n)
