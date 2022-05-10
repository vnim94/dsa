# find pairs of songs where total playing time is multiple of 60

# brute force
def findSongs(A):
    count = 0
    # iterate A
    for i in range(len(A)-1):
        # iterate from i + 1
        for j in range(i+1,len(A)):
            # if sum % 60 is 0, increment count
            if (A[i] + A[j]) % 60 == 0:
                count += 1

    # return count
    return count

# efficient
def findSongs(A):
    count = 0
    mods = {}
    # iterate A
    for value in A:
        mod = value % 60

        # if mod = 0 and 0 in mods (pair exists), add stored value to count
        if mod == 0 and mod in mods:
            count += mods[mod]
        # else if remainder in mods, add stored value to count
        elif 60 - mod in mods:
            count += mods[60 - mod]
        
        # add mod to mods
        mods[mod] = mods.get(mod, 0) + 1


    # return count
    return count


print(findSongs([40,20,30,80])) # (40,20), (40,80)
print(findSongs([60,60,60])) # 3
print(findSongs([15,63,451,213,37,209,343,319])) # 1
print(findSongs([418,204,77,278,239,457,284,263,372,279,476,416,360,18])) # 1