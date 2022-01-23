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

def bestSumUsingTabulation(value, numbers):
    # create table with default value (None)
    s = [None for _ in range(value + 1)]
    
    # seed with base case: value = 0 -> []
    s[0] = []
    
    # loop through table
    for i in range(value + 1):
        # if s[i] has solution, loop through numbers
        if s[i] != None:
            for number in numbers:
                # if i + number within bounds -> if s[i + number] has no solution or len(current solution) > len(possible solution), assign possible solution
                if i + number < value + 1:
                    if s[i + number] == None or len(s[i] + [number]) < len(s[i + number]):
                        s[i + number] = s[i] + [number]

    # return table[value]
    return s[value]

print('Recursion - Memoization - Tabulation')
print(bestSumUsingRecursion(7, [5, 3, 4, 7]), ' - ', bestSumUsingMemoization(7, [5, 3, 4, 7], memo={}) , ' - ', bestSumUsingTabulation(7, [5, 3, 4, 7])) # [7]
print(bestSumUsingRecursion(8, [2, 3, 5]), ' - ', bestSumUsingMemoization(8, [2, 3, 5], memo={}) ,' - ', bestSumUsingTabulation(8, [2, 3, 5])) # [3, 5]
print(bestSumUsingRecursion(8, [1, 4, 5]), ' - ', bestSumUsingMemoization(8, [1, 4, 5], memo={}), ' - ', bestSumUsingTabulation(8, [1, 4, 5])) # [4, 4]
print('-----', ' - ', bestSumUsingMemoization(100, [1, 2, 5, 25], memo={}), ' - ', bestSumUsingTabulation(100, [1, 2, 5, 25])) # [25, 25, 25, 25]

