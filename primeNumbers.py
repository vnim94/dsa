def primeNumbers(n):

	# create array of size n + 1 with 1s to indicate all prime
	primes = [1] * (n + 1)

	# set array[0] and array[1] as 0 (not prime)
	primes[0] = 0
	primes[1] = 0

	# loop through array from index 2 onwards
	for i in range(2, n + 1):
		# if value = 1, set all multiples of that index to 0
		if primes[i] == 1:
			j = 2
			while i * j <= n:
				primes[i * j] = 0
				j += 1

	# loop through array
	for i in range(2, n + 1):
		# print index if value is 1 (prime)
		if primes[i] == 1:
			print(i, end=' ')

primeNumbers(20)
