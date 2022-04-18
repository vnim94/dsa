from xml import dom


def equiLeader(A):
    length = len(A)
    stack = 0
    # find dominator
    for i in range(length):
        if stack == 0:
            stack += 1
            top = i
        elif A[top] != A[i]:
            stack -=1
        else: 
            stack += 1

    if stack > 0:
        return 0
    dominator = A[top]
    # count dominator
    count = 0
    for i in range(length):
        if A[i] == dominator:
            count += 1
    
    if count <= length // 2:
        return 0

    # iterate A and check dominator ratio in both halves. if same, increment count
    dominatorCount = 0
    leaders = 0
    for i in range(length - 1):
        if A[i] == dominator:
            dominatorCount += 1
        leftCount = dominatorCount 
        leftTotal = i + 1
        rightCount = count - dominatorCount
        rightTotal = length - (i + 1)
        if leftCount / leftTotal > 0.5 and rightCount / rightTotal > 0.5:
            leaders += 1

    return leaders

print(equiLeader([4,3,4,4,4,2])) # 2