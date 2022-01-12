def fibonacciUsingRecursion(n):

	if n < 2:
		return n

	return fibonacci(n-1) + fibonacci(n-2)

def fibonacciUsingMemoization(n, memo={}):

	if memo.get(n) != None:
		return memo.get(n)

	if n < 2:
		return n

	memo[n] = fibonacciUsingMemoization(n - 1, memo) + fibonacciUsingMemoization(n - 2, memo)

	return memo.get(n)

def fibonacciUsingTabulation(n):

	s = [0] * (n + 1)
	s[1] = 1

	for i in range(n):
		s[i+1] += s[i]
		if i + 2 < n + 1:
			s[i+2] += s[i]

	return s[n]

print(fibonacciUsingTabulation(10000))
