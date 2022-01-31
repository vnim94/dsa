# find fewest numbers of coins required to make up the amount

def coinChangeUsingRecursion(amount, coins, fewest=None):
	# base case: amount == 0 -> return 0
	if amount == 0:
		return 0	
	# base case: amount < 0 -> return -1
	if amount < 0:
		return -1
	# loop through coins, recursively call using amount - coin	
	for coin in coins:
		result = coinChangeUsingRecursion(amount - coin, coins, fewest)
		if result != -1:
			if fewest == None or fewest > result + 1:
				fewest = result + 1
		else:
			if fewest == None:
				fewest = -1 
	# return fewest
	return fewest

def coinChangeUsingMemoization(amount, coins, fewest=None, memo={}):
	if amount in memo:
		return memo[amount]

	if amount == 0:
		return 0

	if amount < 0:
		return -1

	for coin in coins:
		result = coinChangeUsingMemoization(amount - coin, coins, fewest, memo)
		memo[amount - coin] = result
		if result != -1:
			if fewest == None or fewest > result + 1:
				fewest = result + 1
		else:
			if fewest == None:
				fewest = -1
	
	return fewest

print('Recursion --------------------------')
print(coinChangeUsingRecursion(0, [1])) # 0
print(coinChangeUsingRecursion(3, [2])) # -1
print(coinChangeUsingRecursion(2, [1,2])) # 1
print(coinChangeUsingRecursion(5, [1,2])) # 3
print(coinChangeUsingRecursion(11, [1,2,5])) # 3
print('Memoization ------------------------')
print(coinChangeUsingMemoization(0, [1], memo={})) # 0
print(coinChangeUsingMemoization(3, [2], memo={})) # -1
print(coinChangeUsingMemoization(2, [1,2], memo={})) # 1
print(coinChangeUsingMemoization(5, [1,2], memo={})) # 3
print(coinChangeUsingMemoization(11, [1,2,5], memo={})) # 3
