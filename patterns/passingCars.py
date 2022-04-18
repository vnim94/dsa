# count number of east cars (0) that can be paired with the west cars (1)

def passingCars(A):
    sum = 0
    count = 0
    # iterate A
    for i in range(len(A)):
        # if 0, add to count of east cars
        if A[i] == 0:
            count += 1
        # else add count of east cars to sum of east-west pairs
        else:
            sum += count

    # return sum
    return sum

print(passingCars([0,1,0,1,1])) # 5 