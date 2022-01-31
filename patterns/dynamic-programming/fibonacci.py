def fibUsingRecursion(n):
    if n <= 2:
        return 1

    return fibUsingRecursion(n-1) + fibUsingRecursion(n-2)

def fibUsingMemoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fibUsingMemoization(n-1) + fibUsingMemoization(n-2)
    return memo[n]

def fibUsingTabulation(n):
    s = [0] * (n + 1)
    s[1] = 1

    for i in range(len(s) - 1):
        s[i+1] += s[i]
        if i < len(s) - 2:
            s[i+2] += s[i]

    return s[n]

def fib(n):
    a = b = 1
    num = 0

    for i in range(2, n):
        num = a + b
        a = b
        b = num

    return num

print('Recursion: ', fibUsingRecursion(5))
print('Memoization: ', fibUsingMemoization(8))
print('Tabulation: ', fibUsingTabulation(8))
print('Constant: ', fib(8))
