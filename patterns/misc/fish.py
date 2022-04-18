def fish(A,B):
    downstream = []
    count = 0
    length = len(A)
    # iterate length of arrays
    for i in range(length):
        # if upstream, 
        if B[i] == 0:
            # compare against top of downstream stack while not empty
            while len(downstream) > 0:
                # if value > top, pop, 
                if A[i] > downstream[-1]:
                    downstream.pop()
                # else fish is eaten, so skip
                else:
                    break
            # if no downstream fish, increment count
            else:
                count += 1
        # else add to downstream stack
        else:
            downstream.append(A[i])

    # add remaining downstream fish
    count += len(downstream)

    # return count
    return count

print(fish([4,3,2,1,5],[0,1,0,0,0])) # 2