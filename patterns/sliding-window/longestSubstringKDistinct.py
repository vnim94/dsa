def longestSubstringKDistinct(string, k):
    
    start = 0
    chars = {}
    longest = 0

    # increment end of window 
    for end in range(len(string)):
        # add end to hash table
        chars[string[end]] = chars.get(string[end], 0) + 1
        
        # if criteria exceeded, reduce count of start char, shorten window (increment start)
        if len(chars) > k:
            chars[string[start]] -= 1

            if chars[string[start]] == 0:
                del chars[string[start]]

            start += 1

        # record window size
        length = end + 1 - start
        if length > longest:
            longest = length
    
    # return window size
    return longest

print(longestSubstringKDistinct('araaci', 2)) # 4
print(longestSubstringKDistinct('araaci', 1)) # 2
print(longestSubstringKDistinct('cbbebi', 3)) # 5