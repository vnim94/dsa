def mostFreq(A):
    count = {}
    # iterate A
    for value in A:
        # add count to hash table
        count[value] = count.get(value, 0) + 1
    # iterate hash table and record mostFreq
    max = 0
    mostFreq = None
    for value in count:
        if count[value] > max:
            max = count[value]
            mostFreq = value
    # return mostFreq
    return mostFreq
    
def mostFreq(A):
    # sort
    A.sort()
    max = 0
    count = 0
    mostFreq = None
    # count until new value and check against max
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            count = 0
        count += 1

        if count > max:
            max = count
            mostFreq = A[i]
    # return mostFreq
    return mostFreq

print(mostFreq([1,1,1,1,1,2])) # 1
print(mostFreq([2,3,4,2,5])) # 2
print(mostFreq([2,5,5,6,6,3,3,3])) # 3