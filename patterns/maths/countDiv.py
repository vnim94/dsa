# brute force
# def count(a, b, k):
#     count = 0
#     # iterate from a to b
#     for i in range(a, b + 1):
#         # if i % k = 0, increment count
#         if i % k == 0:
#             count += 1

#     # return count
#     return count

def count(a, b, k):
    if a % k == 0:
        # range floor k + 1
        return (b - a) // k + 1
    # max - (min - midMod) floor k
    return (b - (a - a % k)) // k


print(count(6, 11, 2)) # 3
print(count(11, 345, 17)) # 20
print(count(0, 0, 11)) # 1
print(count(101, 123000000, 10000)) # 12300