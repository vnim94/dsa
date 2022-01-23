def canSumUsingRecursion(target, numbers):

	if target == 0:
		return True

	if target < 0:
		return False

	for number in numbers:
		if canSumUsingRecursion(target - number, numbers):
			return True

	return False

def canSumUsingMemoization(target, numbers, memo={}):

    # if target exists in memo, return value
    if target in memo:
        return memo[target]

    # base cases: == 0 -> true, < 0 -> false
    if target == 0:
        return True

    if target < 0:
        return False	

    # loop through numbers, recursively call target - number
    for number in numbers:
        if canSumUsingMemoization(target - number, numbers, memo):
            return True

    memo[target] = False
    return False

def canSumUsingTabulation(target, numbers):
    # create table of solutions with default values (i.e boolean)
    s = [False] * (target + 1)
    # seed with base base
    s[0] = True
    # loop through cells
    for j in range(target + 1):
        if s[j]: 
            for number in numbers:
                # if current is true, current + number = true
                if j + number < target + 1:
                    s[j + number] = True

    # return cell of target
    return s[target]


print('Recursion - Memoization - Tabulation')
print(canSumUsingRecursion(7, [2, 3]), ' - ', canSumUsingMemoization(7, [2, 3], memo={}), ' - ', canSumUsingTabulation(7, [2, 3])) # true
print(canSumUsingRecursion(7, [5, 3, 4, 7]), ' - ', canSumUsingMemoization(7, [5, 3, 4, 7], memo={}), ' - ', canSumUsingTabulation(7, [5, 3, 4, 7])) # true
print(canSumUsingRecursion(7, [2, 4]), ' - ', canSumUsingMemoization(7, [2, 4], memo={}), ' - ', canSumUsingTabulation(7, [2, 4])) # false 
print(canSumUsingRecursion(8, [2, 3, 5]), ' - ', canSumUsingMemoization(8, [2, 3, 5], memo={}), ' - ', canSumUsingTabulation(8, [2, 3, 5])) # true
print('-----', ' - ', canSumUsingMemoization(300, [7, 14], memo={}), ' - ', canSumUsingTabulation(300, [7, 14])) # false 

