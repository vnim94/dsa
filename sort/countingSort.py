def countingSort(array):

	# find max value
	maxValue = max(array)

	# create count array with length of max + 1
	count = [0] * (maxValue + 1)

	# count each element and store in count array at corresponding index
	for value in array:
		count[value] += 1
	# update values with cumulative sum
	for i in range(len(count) - 1):
		count[i+1] += count[i]
	# shift values in count array to right
	for i in range(len(count) - 1,0,-1):
		count[i] = count[i-1]
	
	count[0] = 0
	# create output array
	output = [0] * len(array)

	# loop through array
	for i in range(len(array)):
		# insert value into output array, index based on count array
		output[count[array[i]]] = array[i]
		# increment value in count array by 1
		count[array[i]] += 1
		
	return output

array = [1,0,3,1,3,1]

print(countingSort(array))

