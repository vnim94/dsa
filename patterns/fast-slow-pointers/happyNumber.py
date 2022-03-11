def happyNumber(num):
    # initialise fast and slow pointers
    slow = num
    fast = num
    # iterate until slow and fast equal. if 1, return true, else false
    while True:
        slow = squareSum(slow)
        fast = squareSum(squareSum(fast))

        if slow == fast:
            break

    if slow == 1:
        return True
    return False

def squareSum(num):
    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += (int(num[i]) ** 2)
    return sum

print(happyNumber(19)) # true
print(happyNumber(2)) # false