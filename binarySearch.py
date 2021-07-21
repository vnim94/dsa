# iterative
def binarySearch(array, x):

	start = 0
	end = len(array) - 1

	while start <= end:
		
		mid = (start + end) // 2
		
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			start = mid + 1
		else:
			end = mid - 1

array = [2, 10, 15, 20, 25]
target = 25

print('Target is at index %d' % binarySearch(array, target)) 

	
