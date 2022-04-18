def check(N):
    # iterate until square <= N
    i = 2
    while i * i <= N:
        # if modulo = 0, return False
        if N % i == 0:
            return False

        i += 1
    # return True
    return True

print(check(13)) # True
print(check(23)) # True
print(check(12)) # False