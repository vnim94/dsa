def quickSort(array, start, end):

	# exit condition
	if start >= end:
		return

	# partition the array
	pIndex = partition(array,start,end)

	# sort left half
	quickSort(array, start, pIndex - 1)

	# sort right half
	quickSort(array, pIndex + 1, end)

	# return the sorted array
	return array

def partition(array, start, end):

	# select last element as pivot
	pivot = array[end]
	index = start

	# loop through elements excluding end / pivot
	for i in range(start, end):
		# if element less than / equal to pivot, swap with element at partition index
		if array[i] <= pivot:
			temp = array[i]
			array[i] = array[index]
			array[index] = temp
		
			index += 1

	# after loop, swap pivot with element at partition index
	temp = array[end]
	array[end] = array[index]
	array[index] = temp
	
	# return the partition index
	return index

array = [7, 4, 6, 2, 3, 5, 1]

print(quickSort(array, 0, len(array) - 1))
