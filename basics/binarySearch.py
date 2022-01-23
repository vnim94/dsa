def iterativeBinarySearch(target, array):
	
	start = 0
	end = len(array) - 1
	
	while start <= end:

		mid = (start + end) // 2
		# mid = target -> return mid
		if array[mid] == target:
			return mid
		# target < array[mid] -> search left (end <- mid)
		if array[mid] > target:
			end = mid - 1
		# target > array[mid] -> search right (start <- mid)
		if array[mid] < target:
			start = mid + 1

	# not found -> return -1
	return -1

print(iterativeBinarySearch(0, [1,2,3])) # -1
print(iterativeBinarySearch(5, [1,2,3,4,5])) # 4
