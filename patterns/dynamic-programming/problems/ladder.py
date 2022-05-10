def ladder(A,B):
    length = len(A)
    result = [0] * length
    solutions = findSolutions(max(A))
    # iterate A
    for i in range(length):
        # add findNumberOfWays(A[i] % 2**B[i]) to result
        result[i] = solutions[A[i]] % 2**B[i]

    # return result
    return result

def findSolutions(rungs):
    # create table of solutions
    s = [0] * (rungs + 1)
    # seed 
    s[0] = 1
    # iterate table
    for i in range(rungs):
        # if possible, iterate options (1 or 2 steps) and add to current solution
        if s[i] > 0:
            s[i+1] += s[i]
            if i + 2 < rungs + 1:
                s[i+2] += s[i]

    # return table[rungs]
    return s

print(ladder([4,4,5,5,1],[3,2,4,3,1])) # [5,1,8,0,1]