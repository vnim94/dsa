def canConstructUsingRecursion(target, strings):
    if target == '':
        return True
    
    for string in strings:
        if target.find(string) == 0:
            suffix = target[len(string):]
            if canConstructUsingRecursion(suffix, strings):
                return True

    return False

def canConstructUsingMemoization(target, strings, memo={}):
    if target in memo:
        return memo[target] 

    if target == '':
        return True

    for string in strings:
        if target.find(string) == 0:
            suffix = target[len(string):]
            if canConstructUsingMemoization(suffix, strings, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

def canConstructUsingTabulation(target, strings):
    # create table with default value (false)
    table = [False for _ in range(len(target) + 1)]
    # seed with base case
    table[0] = True
    # loop through table
    for i in range(len(target) + 1):
        if table[i]:
            for string in strings:
                # if string matches chars starting at i
                if string == target[i:i + len(string)]:
                    table[i + len(string)] = table[i]

    # return table[value]
    return table[len(target)]

print('Recursion - Memoization - Tabulation')
print(canConstructUsingRecursion('ab', ['ab']), ' - ', canConstructUsingMemoization('ab', ['ab'], memo={}), ' - ', canConstructUsingTabulation('ab', ['ab'])) # true
print(canConstructUsingRecursion('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']), ' - ', canConstructUsingMemoization('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={}), ' - ', canConstructUsingTabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # true
print(canConstructUsingRecursion('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), ' - ', canConstructUsingMemoization('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}), ' - ', canConstructUsingTabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # false
print('-------', ' - ', canConstructUsingMemoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'], memo={}), ' - ', canConstructUsingTabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'])) # false