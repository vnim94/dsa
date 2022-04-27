# brute force
def chocolatesByNumbers(N, M):
    eaten = [False for _ in range(N)]

    count = 0
    i = 0
    while not eaten[i]:
        eaten[i] = True
        i += M
        if i > N - 1:
            i = i % N
        count += 1
    
    return count

# least common multiple
def chocolatesByNumbers(N, M):
    return N // gcd(N,M)

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(chocolatesByNumbers(10, 4)) # 5
