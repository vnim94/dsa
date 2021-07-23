def mergeSort(array):

	# if only one element, return array	
	if len(array) == 1:
		return array

	# split the array
	mid = len(array) // 2

	# sort left
	left = mergeSort(array[:mid])
	
	# sort right
	right = mergeSort(array[mid:])
	
	# merge and sort left and right

	return merge(left, right)

def merge(left, right):

	# create temp array and initialise variables
	temp = [None] * (len(left) + len(right))
	i = 0
	j = 0
	index = 0

	# compare elements in left with elements in right
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			temp[index] = left[i]
			i = i + 1
		else:
			temp[index] = right[j]
			j = j + 1

		index = index + 1

	# add remaining elements in left to temp
	while i < len(left):
		temp[index] = left[i]
		i = i + 1

	# add remaining elements in right to temp
	while j < len(right):
		temp[index] = right[j]
		j = j + 1

	return temp


array = [6, 3, 8, 5, 2, 4, 7, 1]

print(mergeSort(array))
