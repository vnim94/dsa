def recursiveMergeSort(array):

	# if array.length = 1 -> return value
	if len(array) == 1:
		return array

	# determine mid
	mid = len(array) // 2

	# sort left
	left = recursiveMergeSort(array[:mid])
	
	# sort right
	right = recursiveMergeSort(array[mid:])
	
	# merge sorted right and left
	merge(left, right, array)

	# return array
	return array


def iterativeMergeSort(array):

	# sub-size = 1
	subSize = 1
	
	# loop while sub-size < array.length
	while subSize < len(array):
		# loop through array until array.length - sub-size
		for i in range(len(array) - subSize):
			# merge adjacent sub-arrays
			left = array[i:i + subSize]
			right = array[i + subSize:i + subSize * 2]
			merge(left, right, array, i)
		# increment sub-size
		subSize *= 2

	# return array
	return array
	
def merge(left, right, array, start):

	i = 0
	j = 0
	k = start

	# loop through left and right until out of bounds
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			j += 1
		k += 1

	# add remaining to array
	while i < len(left):
		array[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		array[k] = right[j]
		j += 1
		k += 1

arrays = [
	[3,1,4,2,8,6,9,7],
	[34,12,78,56,90,99],
	[987,678,456,321,123] # incorrect output
]

for array in arrays:
	print(iterativeMergeSort(array))

