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

print('Recursion ------------------------------------')
print(canConstructUsingRecursion('ab', ['ab'])) # true
print(canConstructUsingRecursion('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # true
print(canConstructUsingRecursion('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # false
# print(canConstructUsingRecursion('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'])) # false
print('Memoization ----------------------------------')
print(canConstructUsingMemoization('ab', ['ab'], memo={}))
print(canConstructUsingMemoization('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo={}))
print(canConstructUsingMemoization('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo={}))
print(canConstructUsingMemoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeee'], memo={})) # false

