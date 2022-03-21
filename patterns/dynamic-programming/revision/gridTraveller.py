from tkinter import Grid


def recursive(row,col):
    # base case: 0 / 0 -> 0
    if row == 0 or col == 0:
        return 0
    # base case: 1 / 1 -> 1
    if row == 1 or col ==1:
        return 1
    # return sum of possible options
    return recursive(row - 1, col) + recursive(row, col - 1)

def memoize(row,col, memo={}):
    if (row,col) in memo:
        return memo[(row,col)]

    if row == 0 or col == 0:
        return 0

    if row == 1 or col == 1:
        return 1

    memo[(row,col)] = memoize(row - 1, col) + memoize(row, col - 1)

    return memo[(row,col)]

def tabulation(row,col):
    # create table (grid in this case)
    grid = [[0 for _ in range(col+1)] for _ in range(row+1)]
    # seed 
    grid[1][1] = 1
    # iterate
    for r in range(row+1):
        for c in range(col+1):
            # add current cell to cell below and cell to right if within bounds
            if r < row:
                grid[r+1][c] += grid[r][c]
            if c < col:
                grid[r][c+1] += grid[r][c] 

    return grid[row][col]

print(recursive(3,3)) # 6
print(memoize(3,3)) # 6
print(tabulation(3,3)) # 6