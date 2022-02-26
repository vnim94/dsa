def longestSubString2Distinct(string):
    # initialise start of window, longest and hash table
    start = 0
    longest = 0
    chars = {}
    # increment end
    for end in range(len(string)): 
        # add char to hash table
        chars[string[end]] = chars.get(string[end], 0) + 1
        # while criteria exceeded (> 2 distinct)
        while len(chars) > 2:
            # reduce count of start char
            chars[string[start]] -= 1
            # if count is zero, delete it
            if chars.get(string[start]) == 0:
                del chars[string[start]]
            # increment start
            start += 1

        # record length
        if end + 1 - start > longest:
            longest = end + 1 - start
        
    # return longest
    return longest

print(longestSubString2Distinct('eceba')) # 3
print(longestSubString2Distinct('ccaabbb')) # 5