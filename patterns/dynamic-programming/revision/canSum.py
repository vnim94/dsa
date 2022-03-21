def recursive(target, values):
    # base case: 0 -> true
    if target == 0:
        return True
    # base case: < 0 -> false
    if target < 0:
        return False
    # iterate options
    for value in values:
        result = recursive(target - value, values)
        if result:
            return True

    return False

def memoize(target, values, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for value in values:
        result = memoize(target - value, values, memo)
        if result:
            return True

    memo[target] = False

    return memo[target]

def tabulation(target, values):
    table = [False for _ in range(target + 1)]
    table[0] = True

    for i in range(target):
        if table[i]:
            for value in values:
                if i + value < target + 1:
                    table[i + value] = True

    return table[target]

print('Recursion - Memoization - Tabulation')
print(recursive(7, [2, 3]), ' - ', memoize(7, [2, 3], memo={}), ' - ', tabulation(7, [2, 3])) # true
print(recursive(7, [5, 3, 4, 7]), ' - ', memoize(7, [5, 3, 4, 7], memo={}), ' - ', tabulation(7, [5, 3, 4, 7])) # true
print(recursive(7, [2, 4]), ' - ', memoize(7, [2, 4], memo={}), ' - ', tabulation(7, [2, 4])) # false 
print(recursive(8, [2, 3, 5]), ' - ', memoize(8, [2, 3, 5], memo={}), ' - ', tabulation(8, [2, 3, 5])) # true
print('-----', ' - ', memoize(300, [7, 14], memo={}), ' - ', tabulation(300, [7, 14])) # false 