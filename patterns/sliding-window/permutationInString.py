from math import perm


def permutation(s1, s2):
    pattern = {}
    # create hashmap of s1
    for letter in s1:
        pattern[letter] = pattern.get(letter, 0) + 1
    
    start = 0
    matchCount = 0
    # sliding window of s2
    for end in range(len(s2)):
        # if letter in s1, decrease letter value in hashmap
        if s2[end] in pattern:
            pattern[s2[end]] -= 1
            # if value is 0, increment matchCount
            if pattern[s2[end]] == 0:
                matchCount += 1
        # if matchCount = number of unique letters, return true
        if matchCount == len(pattern):
            return True
        # if end >= length of s1
        if end >= len(s1) - 1: 
            # if start in s1 and value in hashmap = 0, decrement matchCount and increment value in hashmap
            if s2[start] in pattern:
                if pattern[s2[start]] == 0:
                    matchCount -= 1
                pattern[s2[start]] += 1
            # increment start
            start += 1
    # return false
    return False

print(permutation('ab','eidbaooo')) # true
print(permutation('ab','eidboaoo')) # false
print(permutation('abc','oidbcaf')) # true
print(permutation('dc','odicf')) # false
print(permutation('bcdxabcdy', 'bcdxabcdy')) # true
print(permutation('abc','aaacb')) # true
