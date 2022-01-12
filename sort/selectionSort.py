def selectionSort(array):

	length = len(array)

	for i in range(length):
	
		smallest = i

		for j in range(i, length):
			if array[j] < array[smallest]:
				smallest = j

		temp = array[smallest]
		array[smallest] = array[i]
		array[i] = temp

	return array

array = [5, 5, 3, 8, 2, 9, 1, 4, 7, 6]
						
print(selectionSort(array))
