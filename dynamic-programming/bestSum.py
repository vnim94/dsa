def bestSumUsingRecursion(value, numbers):

	# base case: value = 0 -> return []
	if value == 0:
		return []
	# base case: value < 0 -> return None
	if value < 0:
		return None

	shortest = None

	# loop through numbers, recursively call value - number
	for number in numbers:
		returnValue = bestSumUsingRecursion(value - number, numbers)
		# if result not None and result.length < minLength, set as shortest
		if returnValue != None:
			if shortest == None or len(shortest) > len(returnValue + [number]):
				shortest = returnValue + [number]
				
	# return shortest
	return shortest

def bestSumUsingMemoization(value, numbers, memo={}):
	if value in memo: 
		return memo[value]
	
	if value == 0:
		return []
	
	if value < 0:
 		return None

	shortest = None

	for number in numbers:
		returnValue = bestSumUsingMemoization(value - number, numbers)
		if returnValue != None:
			if shortest == None or len(shortest) > len(returnValue + [number]):
				shortest = returnValue + [number]

	memo[value] = shortest
	return shortest

print('Recursion --------------------------------')
print(bestSumUsingRecursion(7, [5, 3, 4, 7])) # [7]
print(bestSumUsingRecursion(8, [2, 3, 5])) # [3, 5]
print(bestSumUsingRecursion(8, [1, 4, 5])) # [4, 4]
print('Memoization ------------------------------')
print(bestSumUsingMemoization(7, [5, 3, 4, 7], memo={}))
print(bestSumUsingMemoization(8, [2, 3, 5], memo={}))
print(bestSumUsingMemoization(8, [1, 4, 5], memo={}))
print(bestSumUsingMemoization(100, [1, 2, 5, 25], memo={})) # [25, 25, 25, 25]

