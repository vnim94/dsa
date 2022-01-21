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
                totalCombinations.append(combo)

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
            combination = allConstructUsingMemoization(suffix, wordBank, memo)
            for value in combination:
                value.insert(0, string)
                combinations.append(value)

    memo[target] = combinations
    return combinations

print('Recursion ---------------------------------------')
print(allConstructUsingRecursion('hello', ['cat', 'dog', 'mouse'])) # []
print(allConstructUsingRecursion('', ['cat', 'dog', 'mouse'])) # [[]]
print(allConstructUsingRecursion('purple', ['pur','ple'])) # [['pur','ple']]
print(allConstructUsingRecursion('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # [['purp', 'le], ['p', 'ur', 'p', 'le]]
print(allConstructUsingRecursion('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])) # [['ab','cd','ef'], ['abc', 'def'], ['abcd', 'ef'], ['ab', 'c', 'def']]
print(allConstructUsingRecursion('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # []
print(allConstructUsingRecursion('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) # []
print('Memoization ---------------------------------------')
print(allConstructUsingMemoization('hello', ['cat', 'dog', 'mouse'], memo={})) # []
print(allConstructUsingMemoization('', ['cat', 'dog', 'mouse'], memo={})) # [[]]
print(allConstructUsingMemoization('purple', ['pur','ple'], memo={})) # [['pur','ple']]
print(allConstructUsingMemoization('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={})) # [['purp', 'le], ['p', 'ur', 'p', 'le]]
print(allConstructUsingMemoization('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], memo={})) # [['ab','cd','ef'], ['abc', 'def'], ['abcd', 'ef'], ['ab', 'c', 'def']]
print(allConstructUsingMemoization('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={})) # []
print(allConstructUsingMemoization('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], memo={})) # []

