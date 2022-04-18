# brute force
def chocolatesByNumbers(N, M):
    eaten = [False for _ in range(N)]

    count = 0
    i = 0
    while not eaten[i]:
        eaten[0] = True
        i += M
        if i > N - 1:
            i = i % N
        count += 1

    return count

# least common multiple
def chocolatesByNumbers(N, M):
    # find LCM
    lcm = (N * M) // gcd(N,M)
    # divide LCM by M
    return lcm // M

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# print(chocolatesByNumbers(4, 10)) # 5
print(gcd(100, 40))
print(gcd(40, 10))
