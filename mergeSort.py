def mergeSort(array):

	length = len(array)
	# if length = 1, return value
	if length == 1:
		return array[0]

	# mid = length // 2
	mid = length // 2

	# sort left
	left = array[:mid]
	mergeSort(left)

	# sort right
	right = array[mid:]
	mergeSort(right)

	# merge left and right
	merge(left, right, array)

	return array

def merge(left, right, array):

	leftLength = len(left)
	rightLength = len(right)
	i = 0
	j = 0
	k = 0

	# loop through left and right until out of bounds
	while i < leftLength and j < rightLength:
		# if left[i] < right[j], assign to array[k], increment i 
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		# else, assign to array[k], increment j	
		else:
			array[k] = right[j]
			j += 1
		# increment k
		k += 1

	# if leftover in left, loop through and assign to array[k], increment k
	while i < leftLength:
		array[k] = left[i]
		i += 1
		k += 1
	
	# if leftover in right, loop through and assign to array[k], increment k
	while j < rightLength:
		array[k] = right[j]
		j += 1
		k += 1
	
array = [314123415312351235,795,1,3,10,3,5]

print(mergeSort(array))
