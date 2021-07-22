def bubbleSort(array):
	
	while True:
		
		swaps = 0

		for i in range(len(array) - 1):
			if array[i] > array[i + 1]:
				
				swaps = swaps + 1

				temp = array[i + 1]
				array[i + 1] = array[i]
				array[i] = temp

		if swaps == 0:
			break
	
	return array

array = [6, 1, 8, 5, 2, 7, 4, 3]

print(bubbleSort(array))
