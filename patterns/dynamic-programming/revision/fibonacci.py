def recursive(n):
    if n < 3:
        return 1

    return recursive(n - 1) + recursive(n - 2)

def memoize(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 3:
        return 1

    memo[n] = memoize(n-1, memo) + memoize(n-2, memo)

    return memo[n]

def tabulation(n):
    # create table
    table = [0 for _ in range(n+1)]
    # seed 
    table[1] = 1
    # iterate table
    for i in range(n):
        if i < n-1:
            table[i+2] += table[i]
        table[i+1] += table[i]
    
    return table[n]

print('Recursion: ', recursive(8))
print('Memoization: ', memoize(8))
print('Tabulation: ', tabulation(8))
