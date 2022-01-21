def travelUsingRecursion(rows, cols):
	if rows == 0 or cols == 0:
		return 0
	elif rows == 1 or cols == 1:
		return 1
	return travelUsingRecursion(rows - 1, cols) + travelUsingRecursion(rows, cols - 1)

def travelUsingMemoization(rows, cols, memo = {}):

	# use hashmap to store solutions
	if (rows, cols) in memo:
		return memo[(rows,cols)]

	# base case: 0 row / 0 col -> 0 ways
	if rows == 0 or cols == 0:
		return 0
	# base case: 1 row / 1 col -> 1 way
	elif rows == 1 or cols == 1:
		return 1
	# ways = travel(rows - 1, col) + travel(rows, col - 1)
	memo[(rows,cols)] = travelUsingMemoization(rows - 1, cols) + travelUsingMemoization(rows, cols - 1)

	return memo[(rows, cols)]

def travelUsingTabulation(rows, cols):
	# create array to store solutions
    s = []
	# base cases


print('Travelling using recursion: ', travelUsingRecursion(10,10))
print('Travelling using memoization: ', travelUsingMemoization(30,30))
print('Travelling using tabulation: ', travelUsingTabulation(30,30))

