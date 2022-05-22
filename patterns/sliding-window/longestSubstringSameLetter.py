def findLongest(s,k):
    start = 0
    mostFreq = 0
    longest = 0
    letters = {}
    # increment end of window
    for end in range(len(s)):
        # add letter to hashmap and check count against maxCount
        letters[s[end]] = letters.get(s[end],0) + 1
        mostFreq = max(mostFreq, letters[s[end]])
        # if end - count > k, decrement count in hashmap and increment start
        remaining = end + 1 - start - mostFreq
        if remaining > k:
            letters[s[start]] -= 1
            start += 1
        # record longest
        longest = max(longest, end + 1 - start)
    # return maxCount
    return longest 

print(findLongest('aab',1)) # 3
print(findLongest('aabccbb',2)) # 5
print(findLongest('abbcb',1)) # 4
print(findLongest('abccde',1)) # 3