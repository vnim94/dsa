def bubbleSort(array):
	
	smallest = array[0]

	for number in array:
		if number < smallest:
			smallest = number

	while array[0] != smallest:
		for i in range(len(array) - 1):
			if array[i] > array[i + 1]:
				temp = array[i + 1]
				array[i+1] = array[i]
				array[i] = temp

	return array

array = [5, 3, 8, 2, 9]

print(bubbleSort(array))
