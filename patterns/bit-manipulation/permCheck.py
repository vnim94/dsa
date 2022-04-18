# Given an array of n integers, determine if it is a permutation containing 1 to n

def permCheck(A):
    # XOR array
    a = 0
    for i in range(len(A)):
        a ^= A[i]
    # XOR range
    b = 0
    for i in range(1, len(A) + 1):
        b ^= i
    # XOR both should = 0
    return a ^ b == 0

print(permCheck([4,1,3,2])) # true
print(permCheck([4,1,3])) # false