def minCost(cost):
    # base case: n < 2 -> min of cost[0] or cost[1]
    None

def minCost(cost):
    # create table of solutions
    n = len(cost)
    s = [0] * n
    # seed
    s[0] = cost[0]
    s[1] = cost[1]
    # iterate table
    for i in range(2, n):
        # cost at s[i] = cost[i] + min of either s[i-1] or s[i-2]
        s[i] = cost[i] + min(s[i-1], s[i-2])
    # return min of s[n-1] or s[n-2]
    return min(s[n-1], s[n-2])
    
    

print(minCost([10,15,20])) # 15
print(minCost([1,100,1,1,1,100,1,1,100,1])) # 6