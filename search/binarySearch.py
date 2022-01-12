def iterativeBinarySearch(array, target):

	length = len(array)
	start = 0
	end = length - 1

	while start <= end:
		
		mid = (start + end) // 2
	
		if array[mid] == target:
			return 'target found at index ' + str(mid)
		elif array[mid] < target:
			start = mid + 1
		else:
			end = mid - 1

	return 'target not found'

def recursiveBinarySearch(array, target, start, end):

	if start > end:
		return 'target not found'

	mid = (start + end) // 2

	if array[mid] == target:
		return 'target found at index ' + str(mid)
	elif array[mid] < target:
		return recursiveBinarySearch(array, target, mid + 1, end)
	else:
		return recursiveBinarySearch(array, target, start, mid - 1)
	

array = [2, 10, 15, 20, 25]
target = 50

print(recursiveBinarySearch(array, target, 0, 4))
