def howSumUsingRecursion(value, numbers):

	# base case: == 0 -> return [], < 0 -> return None
	if value == 0:
		return []

	if value < 0:
		return None

	# loop through numbers, recursively call with value - number and result
	for number in numbers:
		result = howSumUsingRecursion(value - number, numbers)
		if result != None:
			return result + [number]	

	# return
	return result

def howSumUsingMemoization(value, numbers, memo={}):

	# if in memo, return value
	if value in memo:
		return memo.get(value)

	if value == 0:
		return []

	if value < 0:
		return None

	for number in numbers:
		result = howSumUsingMemoization(value - number, numbers, memo)
		if result != None:
			memo[value] = result + [number]
			return memo.get(value)

	memo[value] = None
	return None

	
print('Recursion -------------------------------')
print(howSumUsingRecursion(0, [1,2,3])) # []
print(howSumUsingRecursion(7, [2,4])) # None
print(howSumUsingRecursion(7, [5,3,4,7])) # [4, 3]
print(howSumUsingRecursion(7, [2,3])) # [3, 2, 2]
print(howSumUsingRecursion(8, [2,3,5])) # [2, 2, 2, 2]
print('Memoization -----------------------------')
#print(howSumUsingMemoization(0, [1,2,3]))
#print(howSumUsingMemoization(7, [5,3,4,7]))
#print(howSumUsingMemoization(7, [2,3]))
#print(howSumUsingMemoization(8, [2,3,5]))
print(howSumUsingMemoization(300, [7, 14])) # None
