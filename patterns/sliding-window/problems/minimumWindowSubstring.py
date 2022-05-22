def minWindow(s, t):
    substring = None
    start = 0
    counter = {}
    
    for letter in t:
        counter[letter] = counter.get(letter, 0) + 1
    
    # increment end while iterating s
    for end in range(len(s)):    
        # if s[end] in t, decrement value. if value is 0, remove from hashmap
        if s[end] in counter:
            counter[s[end]] -= 1
            if counter[s[end]] == 0:
                del counter[s[end]]

        # if len(hashmap) is 0, record s[start:end], increment start and remove first letter (if in t, add back to hashmap)
        if len(counter) == 0:
            if substring == None or end + 1 - start < len(substring):
                substring = s[start:end+1]
                
            if s[start] in t:
                counter[s[start]] = 1
            
            start = end

    # return substring
    if substring == None:
        return ''
    return substring

print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("a", "a")) # "a"
print(minWindow("a", "aa")) # ""
