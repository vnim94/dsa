def stoneWall(A):
    stack = []
    count = 0
    prev = 0
    # iterate A
    for i in range(len(A)):
        # if increasing, set prev as current, increment count and add to stack
        if A[i] > prev:
            prev = A[i]
            count += 1
            stack.append(A[i])
        # if decreasing, empty stack. if stack empty or current != top, requires a new block -> increment count, add to stack 
        elif A[i] < prev:
            while len(stack) > 0 and A[i] < stack[-1]:
                stack.pop()
            if len(stack) == 0 or A[i] != stack[-1]:
                count += 1
                stack.append(A[i])
            # set prev as current
            prev = A[i]
        
    # return count
    return count

print(stoneWall([8,8,5,7,9,8,7,4,8])) # 7