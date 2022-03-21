def recursive(target, words):
    # base case: target = ''
    if target == '':
        return True
    # iterate words
    for word in words:
        prefix = target[:len(word)]
        # recurse with target - word (i.e suffix)
        if word == prefix and recursive(target[len(word):], words):
            return True

    # otherwise false
    return False

def memoize(target, words, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in words:
        prefix = target[:len(word)]
        if word == prefix and memoize(target[len(word):], words, memo):
            return True

    memo[target] = False

    return False

def tabulation(target, words):
    # create table for each char index
    table = [False for _ in range(len(target)+1)]
    table[0] = True

    for i in range(len(target)):
        if table[i]:
            for word in words:
                prefix = target[i:i+len(word)]
                if word == prefix:
                    table[i+len(word)] = True

    return table[len(target)]


print('Recursion - Memoization - Tabulation')
print(recursive('ab', ['ab']), ' - ', 
    memoize('ab', ['ab'], memo={}), ' - ', 
    tabulation('ab', ['ab'])) # true
print(recursive('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']), ' - ', 
    memoize('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={}), ' - ', 
    tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # true
print(recursive('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), ' - ', 
    memoize('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}), ' - ', 
    tabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # false
print('-------', ' - ', 
    memoize('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'], memo={}), ' - ', 
    tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'])) # false