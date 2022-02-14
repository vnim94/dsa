def climbUsingRecursion(steps):
    # base case: 0 or 1 -> 1
    if steps < 2:
        return 1

    count = 0

    # loop through possible options (1, 2)
    for i in range(1, 3):
        count += climbUsingRecursion(steps - i)
    
    # return count
    return count

def climbUsingMemoization(steps, memo={}):
    # if in memo, return value
    if steps in memo:
        return memo[steps]

    if steps < 2:
        return 1

    count = 0

    for i in range(1, 3):
        count += climbUsingMemoization(steps - i, memo)

    memo[steps] = count
    return count

def climbUsingTabulation(steps):
    # create table to store solutions
    table = [0] * (steps + 1)
    # seed table with base case (0 -> 1)
    table[0] = 1
    # loop through table
    for i in range(steps):
        # if table[i] has solution, table[i + 1] and table[i + 2] are possible as well
        if table[i] > 0:
            # loop through possible options
            for j in range(1,3):
                # check if within bounds
                if i + j < steps + 1:
                    # add existing solution
                    table[i + j] += table[i]

    # return table[steps]
    return table[steps]

print(climbUsingRecursion(2), climbUsingMemoization(2), climbUsingTabulation(2)) # 2
print(climbUsingRecursion(3), climbUsingMemoization(3), climbUsingTabulation(3)) # 3