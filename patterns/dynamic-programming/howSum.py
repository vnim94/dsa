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
		return memo[value]

	if value == 0:
		return []

	if value < 0:
		return None

	for number in numbers:
		result = howSumUsingMemoization(value - number, numbers, memo)
		if result != None:
			memo[value] = result + [number]
			return memo[value]

	memo[value] = None
	return None

def howSumUsingTabulation(value, numbers):
    # create table to store solutions with default value (None)
    s = [None for _ in range(value + 1)]
    # seed with base case: value = 0 -> []
    s[0] = []
    # loop through table
    for i in range(value + 1):
        if s[i]:
            for number in numbers:
                if i + number < value + 1:
                    s[i + number] = s[i] + [number]

    # return table[value]
    return s[value]

print('Recursion - Memoization - Tabulation')
print(howSumUsingRecursion(7, [2, 3]), ' - ', howSumUsingMemoization(7, [2, 3], memo={}), ' - ', howSumUsingTabulation(7, [2, 3])) # None
print(howSumUsingRecursion(7, [5, 3, 4, 7]), ' - ', howSumUsingMemoization(7, [5, 3, 4, 7], memo={}), ' - ', howSumUsingTabulation(7, [5, 3, 4, 7])) # [4, 3]
print(howSumUsingRecursion(7, [2, 4]), ' - ', howSumUsingMemoization(7, [2, 4], memo={}), ' - ', howSumUsingTabulation(7, [2, 4])) # None 
print(howSumUsingRecursion(8, [2, 3, 5]), ' - ', howSumUsingMemoization(8, [2, 3, 5], memo={}), ' - ', howSumUsingTabulation(8, [2, 3, 5])) # [2, 2, 2, 2]
print('-----', ' - ', howSumUsingMemoization(300, [7, 14], memo={}), ' - ', howSumUsingTabulation(300, [7, 14])) # None 
