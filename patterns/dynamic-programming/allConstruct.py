def allConstructUsingRecursion(target, wordBank):
    # base case: target = '' -> return []
    if target == '':
        return [[]]

    totalCombinations = []

    # loop through strings in wordbank
    for string in wordBank:
    # if string is a prefix, recursively call with suffix
        if target.find(string) == 0:
            suffix = target[len(string):]
            combinations = allConstructUsingRecursion(suffix, wordBank)
            for combo in combinations:
                combo.insert(0, string)
            totalCombinations += combinations

    return totalCombinations

def allConstructUsingMemoization(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
        
    if target == '':
        return [[]]

    combinations = []

    for string in wordBank:
        if target.find(string) == 0:
            suffix = target[len(string):]
            suffixWays = allConstructUsingMemoization(suffix, wordBank, memo)
            targetWays = []
            for value in suffixWays:
                targetWays.append([string] + value)
            combinations += targetWays
            
    memo[target] = combinations
    return combinations

def allConstructUsingTabulation(target, wordBank):
    # array with default value []
    table = [[] for _ in range(len(target) + 1)]
    
    # base case: '' -> [[]]
    table[0] = [[]]
    
    # loop table
    for i in range(len(target) + 1):
        # if table[i].length > 0, loop through words
        if len(table[i]) > 0:
            for word in wordBank:
            # if word matches chars starting from i, add to array of table[i]
                if word == target[i:i + len(word)]:
                    for element in table[i]:
                        table[i + len(word)].append(element + [word])
                    

    # return table[len(target)]
    return table[len(target)]

print('Recursion - Memoization - Tabulation')
print(allConstructUsingRecursion('hello', ['cat', 'dog', 'mouse']), ' - ', allConstructUsingMemoization('hello', ['cat', 'dog', 'mouse'], memo={}), ' - ', allConstructUsingTabulation('hello', ['cat', 'dog', 'mouse'])) # []
print(allConstructUsingRecursion('', ['cat', 'dog', 'mouse']), ' - ', allConstructUsingMemoization('', ['cat', 'dog', 'mouse'], memo={}), ' - ', allConstructUsingTabulation('', ['cat', 'dog', 'mouse'])) # [[]]
print(allConstructUsingRecursion('purple', ['pur','ple']), ' - ', allConstructUsingMemoization('purple', ['pur','ple'], memo={}) , ' - ', allConstructUsingTabulation('purple', ['pur','ple'])) # [['pur','ple']]
print(allConstructUsingRecursion('purple', ['purp', 'p', 'ur', 'le', 'purpl']), ' - ', allConstructUsingMemoization('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}), ' - ', allConstructUsingTabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # [['purp', 'le], ['p', 'ur', 'p', 'le]]
print(allConstructUsingRecursion('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']), ' - ', allConstructUsingMemoization('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], memo={}), ' - ', allConstructUsingTabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) ) # [['ab','cd','ef'], ['abc', 'def'], ['abcd', 'ef'], ['ab', 'c', 'def']]
print(allConstructUsingRecursion('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), ' - ', allConstructUsingMemoization('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}) , ' - ', allConstructUsingTabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # []
print('--------', ' - ', allConstructUsingMemoization('aaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], memo={}) ,' - ', allConstructUsingTabulation('aaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) # []
