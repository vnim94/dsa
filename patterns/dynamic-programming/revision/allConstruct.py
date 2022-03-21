def recursive(target, words):
    # base case: target = '' -> []
    if target == '':
        return [[]]

    combos = []
    # iterate options
    for word in words:
        prefix = target[:len(word)]
        # if word = prefix, recurse with suffix
        if word == prefix:
            combo = recursive(target[len(word):], words)
            for value in combo:
                value.insert(0, word)
            combos += combo

    # return combos
    return combos

def memoize(target, words, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    combos = []

    for word in words:
        prefix = target[:len(word)]
        if word == prefix:
            combo = memoize(target[len(word):], words, memo)
            new = []
            for c in combo:
                new.append([word] + c)
            combos += new
    
    memo[target] = combos
    return memo[target]

def tabulation(target, words):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        if len(table[i]) > 0:
            for word in words:
                prefix = target[i:i+len(word)]
                if word == prefix: 
                    for c in table[i]:
                        table[i + len(word)].append(c + [word])

    return table[len(target)]

print('Recursion - Memoization - Tabulation')
print(recursive('hello', ['cat', 'dog', 'mouse']), ' - ', 
    memoize('hello', ['cat', 'dog', 'mouse'], memo={}), ' - ', 
    tabulation('hello', ['cat', 'dog', 'mouse'])) # []
print(recursive('', ['cat', 'dog', 'mouse']), ' - ', 
    memoize('', ['cat', 'dog', 'mouse'], memo={}), ' - ', 
    tabulation('', ['cat', 'dog', 'mouse'])) # [[]]
print(recursive('purple', ['pur','ple']), ' - ', 
    memoize('purple', ['pur','ple'], memo={}) , ' - ', 
    tabulation('purple', ['pur','ple'])) # [['pur','ple']]
print(recursive('purple', ['purp', 'p', 'ur', 'le', 'purpl']), ' - ', 
    memoize('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}), ' - ', 
    tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # [['purp', 'le], ['p', 'ur', 'p', 'le]]
print(recursive('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']), ' - ', 
    memoize('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], memo={}), ' - ', 
    tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) ) # [['ab','cd','ef'], ['abc', 'def'], ['abcd', 'ef'], ['ab', 'c', 'def']]
print(recursive('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), ' - ', 
    memoize('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}) , ' - ', 
    tabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # []
print('--------', ' - ', 
    memoize('aaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], memo={}) ,' - ', 
    tabulation('aaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) # []