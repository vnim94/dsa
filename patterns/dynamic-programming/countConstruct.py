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

def countConstructUsingTabulation(target, wordBank):
    # table with default value (0)
    table = [0 for _ in range(len(target) + 1)]
    # seed with base case: '' -> 1  
    table[0] = 1
    # loop table
    for i in range(len(target) + 1):
        # if table[i] > 0, loop through words
        if table[i] > 0:
            for word in wordBank:
            # if word matches chars starting from i, add table[i] to table[i+len(word)]
                if word == target[i:i + len(word)]:
                    table[i + len(word)] += table[i]

    # return table[len(target)]
    return table[len(target)]
     

print('Recursion - Memoization - Tabulation')
print(countConstructUsingRecursion('abcd', ['de']), ' - ', countConstructUsingMemoization('abcd', ['de'], memo={}), ' - ', countConstructUsingTabulation('abcd', ['de'])) # 0
print(countConstructUsingRecursion('abcd', ['ab','cd']), ' - ', countConstructUsingMemoization('abcd', ['ab','cd'], memo={}), ' - ', countConstructUsingTabulation('abcd', ['ab','cd'])) # 1
print(countConstructUsingRecursion('abcdef', ['ab','abc','cd','def','abcd']), ' - ', countConstructUsingMemoization('abcdef', ['ab','abc','cd','def','abcd'], memo={}) , ' - ', countConstructUsingTabulation('abcdef', ['ab','abc','cd','def','abcd'])) # 1
print(countConstructUsingRecursion('purple', ['purp', 'p', 'ur', 'le', 'purpl']), ' - ', countConstructUsingMemoization('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo={}) , ' - ', countConstructUsingTabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']) ) # 2
print(countConstructUsingRecursion('skateboard',['bo','rd','ate','t','ska','sk','boar']), ' - ', countConstructUsingMemoization('skateboard',['bo','rd','ate','t','ska','sk','boar'], memo={}) , ' - ' , countConstructUsingTabulation('skateboard',['bo','rd','ate','t','ska','sk','boar'])) # 0
print(countConstructUsingRecursion('enterapotentpot', ['a','p','ent','enter','ot','o','t']), ' - ', countConstructUsingMemoization('enterapotentpot', ['a','p','ent','enter','ot','o','t'], memo={}) , ' - ', countConstructUsingTabulation('enterapotentpot', ['a','p','ent','enter','ot','o','t'])) # 4
print('--------', ' - ', countConstructUsingMemoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'eeeeee'], memo={}), ' - ', countConstructUsingTabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'eeeeee'])) # 0
