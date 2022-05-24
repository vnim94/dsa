def countNonDivisors(A):
    count = {}
    # create hashmap of values : count
    for value in A:
        count[value] = count.get(value,0) + 1

    divisors = {}
    # create hashmap of value : divisors 
    for value in A:
        if value == 1:
            divisors[value] = [1]
        else:
            divisors[value] = [1, value]

    i = 2
    maxValue = max(A)
    # using sieve, iterate while i * i <= max
    while i * i <= maxValue:
        j = i
        # iterate while i <= max
        while j <= maxValue:
            # if i in divisors and i not in divisors of i, add i to divisors and other factor
            if j in divisors and i not in divisors[j]:
                divisors[j].append(i)
                divisors[j].append(j // i)
            # increment i by i
            j += i
        i += 1

    # iterate divisors and append to output
    output = [0] * len(A)
    for i in range(len(A)):
        # non-divisors = length - count of divisors
        divisorCount = 0
        for div in divisors[A[i]]:
            divisorCount += count.get(div,0)
        output[i] = len(A) - divisorCount

    # return output
    return output

print(countNonDivisors([3,1,2,3,6])) # [2,4,3,2,0]