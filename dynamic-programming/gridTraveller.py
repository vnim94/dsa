def travelUsingRecursion(rows, col)
	if rows == 0 or cols == 0:
		return 0
	elif rows == 1 or cols == 1:
		return 1
	return travelUsingRecursion(rows - 1, cols) + travelUsingRecursion(rows, cols - 1)

def travelUsingMemoization(rows, cols, s = {}):

	# use hashmap to store solutions
	if s.get((rows,cols)):
		return s.get((rows,cols))

	# base case: 0 row / 0 col -> 0 ways
	if rows == 0 or cols == 0:
		return 0
	# base case: 1 row / 1 col -> 1 way
	elif rows == 1 or cols == 1:
		return 1
	# ways = travel(rows - 1, col) + travel(rows, col - 1)
	s[(rows,cols)] = travel(rows - 1, cols) + travel(rows, cols - 1)

	return s.get((rows,cols))

def travelUsingTabulation(rows, cols):

	# create array to store solutions

	# base cases


print('Travelling using recursion: ', travelUsingRecursion(30,30))
print('Travelling using recursion + memoization: ', travelUsingMemoization(30,30))
print('Travelling using tabulation: ', travelUsingMemoization(30,30))

