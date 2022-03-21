def recursive(target, values):
    # base case: 0 -> [], < 0 -> None
    if target == 0:
        return []
    if target < 0:
        return None
    
    # iterate values
    for value in values:
        # recurse target - value
        result = recursive(target - value, values)
        # if return value not none, add target to result
        if result != None:
            return result + [value]

    return None

def memoize(target, values, memo={}):
    if target in memo:
        return memo[target]
    
    if target == 0:
        return []
    if target < 0:
        return None

    for value in values:
        result = memoize(target - value, values, memo)
        if result != None:
            return result + [value]

    memo[target] = None
    return memo[target]

def tabulation(target, values):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(target):
        if table[i] != None:
            for value in values:
                if i + value < target + 1:
                    table[i + value] = table[i] + [value]

    return table[target]


print('Recursion - Memoization - Tabulation')
print(recursive(7, [2, 3]), ' - ', memoize(7, [2, 3], memo={}), ' - ', tabulation(7, [2, 3])) # [3, 2, 2]
print(recursive(7, [5, 3, 4, 7]), ' - ', memoize(7, [5, 3, 4, 7], memo={}), ' - ', tabulation(7, [5, 3, 4, 7])) # [4, 3]
print(recursive(7, [2, 4]), ' - ', memoize(7, [2, 4], memo={}), ' - ', tabulation(7, [2, 4])) # None 
print(recursive(8, [2, 3, 5]), ' - ', memoize(8, [2, 3, 5], memo={}), ' - ', tabulation(8, [2, 3, 5])) # [2, 2, 2, 2]
print('-----', ' - ', memoize(300, [7, 14], memo={}), ' - ', tabulation(300, [7, 14])) # None 