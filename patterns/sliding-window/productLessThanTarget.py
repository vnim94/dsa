def productLessThanTarget(array, target):
    None

print(productLessThanTarget([2, 5, 3, 10], 30)) # [2], [5], [2, 5], [3], [5, 3], [10] 
print(productLessThanTarget([8, 2, 6, 5], 50)) # [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
print(productLessThanTarget([10, 5, 2, 6], 100)) # [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].