def longestSubstringNoRepeat(s):
    # initialise start, longest and seen
    start = 0
    end = 0
    longest = 0
    seen = {}
    # increment end of window while start less than or equal to
    while start <= end and end < len(s):
        # if not in seen, add letter and record longest
        if s[end] not in seen:
            seen[s[end]] = True
            if end + 1 - start > longest:
                longest = end + 1 - start
            end += 1
        # else, remove starting letter from seen and increment start
        else:
            del seen[s[start]]
            start += 1

    # return longest
    return longest


print(longestSubstringNoRepeat('abcabcbb')) # abc -> 3
print(longestSubstringNoRepeat('bbbbb')) # b -> 1
print(longestSubstringNoRepeat('pwwkew')) # wke -> 3
print(longestSubstringNoRepeat('abcdef')) # abcdef -> 6
print(longestSubstringNoRepeat('aab')) # ab -> 2
print(longestSubstringNoRepeat('dvdf')) # vdf -> 3
