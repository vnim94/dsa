def recursive(target, words):
    # base case: target = '' -> return 1
    if target == '':
        return 1

    count = 0

    # iterate options
    for word in words:
        prefix = target[:len(word)]
        # if prefix matches, recurse with suffix
        if word == prefix:
            count += recursive(target[len(word):], words)
            
    # return count
    return count

def memoize(target, words, memo={}):
    if target in memo:
        return memo[target]

    if target == '':
        return 1

    count = 0

    for word in words:
        prefix = target[:len(word)]
        if word == prefix:
            count += memoize(target[len(word):], words, memo)

    memo[target] = count
    return memo[target]

def tabulation(target, words):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target)):
        if table[i] > 0:
            for word in words:
                prefix = target[i:i+len(word)]
                if word == prefix and i + len(word) < len(target) + 1:
                    table[i + len(word)] += table[i]
                    
    return table[len(target)]

print('Recursion - Memoization - Tabulation')
print(recursive('abcd', ['de']), ' - ', 
    memoize('abcd', ['de'], memo={}), ' - ', 
    tabulation('abcd', ['de'])) # 0
print(recursive('abcd', ['ab','cd']), ' - ', 
    memoize('abcd', ['ab','cd'], memo={}), ' - ', 
    tabulation('abcd', ['ab','cd'])) # 1
print(recursive('abcdef', ['ab','abc','cd','def','abcd']), ' - ', 
    memoize('abcdef', ['ab','abc','cd','def','abcd'], memo={}) , ' - ', 
    tabulation('abcdef', ['ab','abc','cd','def','abcd'])) # 1
print(recursive('purple', ['purp', 'p', 'ur', 'le', 'purpl']), ' - ', 
    memoize('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}) , ' - ', 
    tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']) ) # 2
print(recursive('skateboard',['bo','rd','ate','t','ska','sk','boar']), ' - ', 
    memoize('skateboard',['bo','rd','ate','t','ska','sk','boar'], memo={}) , ' - ' , 
    tabulation('skateboard',['bo','rd','ate','t','ska','sk','boar'])) # 0
print(recursive('enterapotentpot', ['a','p','ent','enter','ot','o','t']), ' - ', 
    memoize('enterapotentpot', ['a','p','ent','enter','ot','o','t'], memo={}) , ' - ', 
    tabulation('enterapotentpot', ['a','p','ent','enter','ot','o','t'])) # 4
print('--------', ' - ', 
    memoize('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'eeeeee'], memo={}), ' - ', 
    tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'eeeeee'])) # 0