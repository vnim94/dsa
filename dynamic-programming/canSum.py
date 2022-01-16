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
	if memo.get(target):
		return memo.get(target)

	# base cases: == 0 -> true, < 0 -> false
	if target == 0:
		return True
	
	if target < 0:
		return False	
	
	# loop through numbers, recursively call target - number
	for number in numbers:
		memo[target] = canSumUsingMemoization(target - number, numbers, memo)
	
	return memo.get(target)

#print(canSumUsingRecursion(7, [5,3,4,7]))
#print(canSumUsingRecursion(7, [2,4]))
#print(canSumUsingMemoization(7, [5,3,4,7]))
print(canSumUsingMemoization(7, [2,4]))


