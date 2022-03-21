def recursive(target, numbers):
    # base case: target = 0: return []
    if target == 0:
        return []
    # base case: target < 0: return None
    if target < 0:
        return None

    shortest = None

    # iterate numbers
    for num in numbers:
        result = recursive(target - num, numbers)
        if result != None:
            if shortest == None or len(shortest) > len([num] + result):
                shortest = [num] + result

    # return shortest subset
    return shortest

def memoize(target, numbers, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    shortest = None

    for num in numbers:
        result = memoize(target - num, numbers, memo)
        if result != None:
            if shortest == None or len(shortest) > len([num] + result):
                shortest = [num] + result

    memo[target] = shortest
    return memo[target]

def tabulation(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(target):
        if table[i] != None:
            for num in numbers:
                if i + num < target + 1:
                    if table[i+num] == None or len(table[i] + [num]) < len(table[i + num]):
                        table[i+num] = table[i] + [num]

    return table[target]

print('Recursion - Memoization - Tabulation')
print(recursive(7, [5, 3, 4, 7]), ' - ', 
    memoize(7, [5, 3, 4, 7], memo={}) , ' - ', 
    tabulation(7, [5, 3, 4, 7])) # [7]
print(recursive(8, [2, 3, 5]), ' - ', 
    memoize(8, [2, 3, 5], memo={}) ,' - ', 
    tabulation(8, [2, 3, 5])) # [3, 5]
print(recursive(8, [1, 4, 5]), ' - ', 
    memoize(8, [1, 4, 5], memo={}), ' - ', 
    tabulation(8, [1, 4, 5])) # [4, 4]
print('-----', ' - ', 
    memoize(100, [1, 2, 5, 25], memo={}), ' - ', 
    tabulation(100, [1, 2, 5, 25])) # [25, 25, 25, 25]

    