def countConstructUsingRecursion(target, wordBank):

	# base case: target = '' -> return 1
	if target == '':
		return 1

	count = 0

	# loop through strings
	for string in wordBank:
		# if string is a suffix, recursively call with suffix as target
		if target.find(string) == 0:
			suffix = target[len(string):]
			count += countConstructUsingRecursion(suffix, wordBank)
				
	# if no possible combinations, return 0
	return count

def countConstructUsingMemoization(target, wordBank, memo={}):

	if target in memo:
		return memo[target]

	if target == '':
		return 1

	count = 0

	for string in wordBank:
		if target.find(string) == 0:
			suffix = target[len(string):]
			count += countConstructUsingMemoization(suffix, wordBank, memo)

	memo[target] = count
	return count

print('Recursion ---------------------------------------')
print(countConstructUsingRecursion('abcd', ['de'])) # 0
print(countConstructUsingRecursion('abcd', ['ab','cd'])) # 1
print(countConstructUsingRecursion('abcdef', ['ab','abc','cd','def','abcd'])) # 1
print(countConstructUsingRecursion('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 2
print(countConstructUsingRecursion('skateboard',['bo','rd','ate','t','ska','sk','boar'])) # 0
print(countConstructUsingRecursion('enterapotentpot', ['a','p','ent','enter','ot','o','t'])) # 4

print('Memoization --------------------------------------')
print(countConstructUsingMemoization('abcd', ['de'], memo={})) # 0
print(countConstructUsingMemoization('abcd', ['ab','cd'], memo={})) # 1
print(countConstructUsingMemoization('abcdef', ['ab','abc','cd','def','abcd'], memo={})) # 1
print(countConstructUsingMemoization('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={})) # 2
print(countConstructUsingMemoization('skateboard',['bo','rd','ate','t','ska','sk','boar'], memo={})) # 0
print(countConstructUsingMemoization('enterapotentpot', ['a','p','ent','enter','ot','o','t'], memo={})) # 4
print(countConstructUsingMemoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
	'e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'eeeeee'
], memo={})) # 0