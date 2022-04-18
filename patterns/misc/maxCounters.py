def solution(N, A):
    # result, max, maxCounter and updated flag
    result = [0] * N
    max = 0
    maxCounter = 0
    updated = False

    # iterate A
    for i in range(len(A)):
        # if A[i] is N + 1, reset result, add current max to maxCounter, reset max and set updated flag
        if not updated and A[i] == N + 1:
            result = [0] * N
            maxCounter += max
            max = 0
            updated = True
        # else add A[i] to index+1, record max and set updated flag
        elif A[i] - 1 < N:
            result[A[i] - 1] += 1
            if result[A[i] - 1] > max:
                max = result[A[i] - 1]
            updated = False

    # add maxCounter to values in result
    for i in range(N):
        result[i] += maxCounter

    # return result
    return result

print(solution(5, [3, 4, 4, 6, 1, 4, 4])) # [3,2,2,4,2]