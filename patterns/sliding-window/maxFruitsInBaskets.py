def maxFruitsInBaskets(trees):
    
    start = 0
    types = {}
    max = 0

    # increment window size 
    for end in range(len(trees)):
        # add value to hash table
        types[trees[end]] = types.get(trees[end], 0) + 1
        # if criteria exceeded (> 2 types), reduce count of start value, shrink window size
        if len(types) > 2:
            types[trees[start]] -= 1
            
            if types[trees[start]] == 0:
                del types[trees[start]]

            start += 1
        
        # record window size if > max
        length = end + 1 - start
        if length > max:
            max = length

    # return max
    return max

print(maxFruitsInBaskets(['A', 'B', 'C', 'A', 'C'])) # 3
print(maxFruitsInBaskets(['A', 'B', 'C', 'B', 'B', 'C'])) # 5