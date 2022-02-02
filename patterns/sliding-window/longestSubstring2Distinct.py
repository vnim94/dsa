def longestSubString2Distinct(string):

    start = 0
    chars = {}
    longest = 0

    # increment window size until criteria met
    for end in range(len(string)):
        # record count of each character in a hash table
        chars[string[end]] = chars.get(string[end], 0) + 1
        
        # while criteria exceeded 
        while len(chars) > 2:
            # decrease count of starting char
            chars[string[start]] -= 1
            
            if chars[string[start]] == 0:
                del chars[string[start]]
            
            # increment start
            start += 1
            
        # once criteria met, record window size 
        length = end + 1 - start
        if length > longest:
            longest = length

    # return max window size
    return longest

print(longestSubString2Distinct('eceba')) # 3
print(longestSubString2Distinct('ccaabbb')) # 5