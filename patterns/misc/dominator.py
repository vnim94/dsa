def dominator(A):
    length = len(A)
    stack = 0
    # iterate length of A
    for i in range(length):
        # if stack = 0, increment stack of stack and set top as A[i]
        if stack == 0:
            stack += 1
            top = i
        # else if top != to A[i], decrement stack
        elif A[top] != A[i]:
            stack -= 1
        # else increment stack
        else:
            stack += 1

    # if stack not empty (i.e stack > 0), set top as the dominator
    if stack > 0:
        dominator = top
    # iterate A and count freq of dominator
    count = 0
    for i in range(length):
        if A[i] == A[dominator]:
            count += 1
    # if freq > half of length, return dominator
    if count > length // 2:
        return dominator
    # else return -1
    return -1

print(dominator([3,4,3,2,3,-1,3,3])) # 0 / 2 / 4 / 6 / 7
print(dominator([])) # -1