# find fewest numbers of coins required to make up the amount

def coinChangeUsingRecursion(amount, coins):
    # base case: amount == 0 -> return 0
    if amount == 0:
        return 0	
    # base case: amount < 0 -> return -1
    if amount < 0:
        return -1

    fewest = None

    # loop through coins, recursively call using amount - coin	
    for coin in coins:
        result = coinChangeUsingRecursion(amount - coin, coins)
        if result != -1:
            if fewest == None or fewest > result + 1:
                fewest = result + 1
        else:
            if fewest == None:
                fewest = -1 
    # return fewest
    return fewest

def coinChangeUsingMemoization(amount, coins, memo={}):
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    if amount < 0:
        return -1

    fewest = None

    for coin in coins:
        result = coinChangeUsingMemoization(amount - coin, coins, memo)
        memo[amount - coin] = result
        if result != -1:
            if fewest == None or fewest > result + 1:
                fewest = result + 1
        else:
            if fewest == None:
                fewest = -1

    return fewest

def coinChangeUsingTabulation(amount, coins):
    # create table to store solutions
    table = [-1 for _ in range(amount + 1)] 
    # seed table with base case (0 -> 0)
    table[0] = 0
    # loop through table
    for i in range(amount + 1):
        # if table[i] possible, table[i + option] is also possible
        if table[i] > -1:
            for coin in coins:
                # check amount within bounds
                if i + coin < amount + 1:
                    # if no existing solution for the amount OR current solution < existing solution, replace with current solution
                    if table[i + coin] == -1 or table[i] + 1 < table[i + coin]:
                        table[i + coin] = table[i] + 1

    # return table[amount]
    return table[amount]

print('Recursion - Memoization - Tabulation')
print(coinChangeUsingRecursion(0, [1]), ' - ', coinChangeUsingMemoization(0, [1], memo={}), ' - ', coinChangeUsingTabulation(0, [1])) # 0
print(coinChangeUsingRecursion(3, [2]), ' - ', coinChangeUsingMemoization(3, [2], memo={}), ' - ', coinChangeUsingTabulation(3, [2])) # -1
print(coinChangeUsingRecursion(2, [1,2]), ' - ', coinChangeUsingMemoization(2, [1,2], memo={}), ' - ', coinChangeUsingTabulation(2, [1,2])) # 1
print(coinChangeUsingRecursion(5, [1,2]), ' - ', coinChangeUsingMemoization(5, [1,2], memo={}), ' - ', coinChangeUsingTabulation(5, [1,2])) # 3
print(coinChangeUsingRecursion(11, [1,2,5]), ' - ', coinChangeUsingMemoization(11, [1,2,5], memo={}), ' - ', coinChangeUsingTabulation(11, [1,2,5])  ) # 3
