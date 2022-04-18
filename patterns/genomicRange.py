# find minimal impact factor for given genomic range

# brute force
def genomicRange(S, P, Q):
    # create map of impact factors
    impact = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }
    result = [0] * len(P)
    min = 4
    # iterate P and Q
    for i in range(len(P)):
        # iterate P[i] to Q[i] and record min
        for j in range(P[i],Q[i]+1):
            if impact[S[j]] < min:
                min = impact[S[j]]
    
        result[i] = min
        min = 4
    # return result
    return result

# efficient
def genomicRange(S, P, Q):
    length = len(S)

    # create array for each nucleotide of length S
    A = [0] * length
    C = [0] * length
    G = [0] * length
    T = [0] * length

    for i in range(length):
        if S[i] == 'A':
            A[i] += 1
        elif S[i] == 'C':
            C[i] += 1
        elif S[i] == 'G':
            G[i] += 1
        else:
            T[i] += 1

    # cumulative sum each array (count of nucleotide at each index of S)
    for i in range(1,length):
        A[i] += A[i-1]
        C[i] += C[i-1]
        G[i] += G[i-1]
        T[i] += T[i-1]

    result = [0] * len(P)
    # iterate P and Q
    for i in range(len(P)):
        # check values in nucleotide arrays. 
        # if P-value = Q-value, add P-value impact factor
        if P[i] == Q[i]:
            if S[P[i]] == 'A':
                result[i] += 1
            elif S[P[i]] == 'C':
                result[i] += 2
            elif S[P[i]] == 'G':
                result[i] += 3
            elif S[P[i]] == 'T':
                result[i] += 4
        # if P-value < Q-value or single occurrence of nucleotide, add impact factor to result
        if A[P[i]] < A[Q[i]] or S[P[i]] == 'A': 
            result[i] = 1
        elif C[P[i]] < C[Q[i]] or S[P[i]] == 'C':
            result[i] = 2
        elif G[P[i]] < G[Q[i]] or S[P[i]] == 'G':
            result[i] = 3
        elif T[P[i]] < T[Q[i]] or S[P[i]] == 'T':
            result[i] = 4

    return result

print(genomicRange('CAGCCTA', [2,5,0], [4,5,6])) # [2, 4, 1]