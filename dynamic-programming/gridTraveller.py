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
	# create table to store solutions
    s = []
    for _ in range(rows):
        a = []
        for _ in range(cols):
            a.append(0)
        s.append(a)
    
    # base case: 1 row / 1 col -> 1 way
    s[0][0] = 1
    # loop through table, 
    for row in range(rows):
        for col in range(cols):
            # add value of current cell to bottom and right cells
            if row + 1 < rows:
                s[row + 1][col] += s[row][col]
            if col + 1 < cols:
                s[row][col + 1] += s[row][col]

    # return value at cell (rows, cols)
    return s[rows-1][cols-1]

print('Travelling using recursion: ', travelUsingRecursion(10,10))
print('Travelling using memoization: ', travelUsingMemoization(500,500))
print('Travelling using tabulation: ', travelUsingTabulation(700,700))

