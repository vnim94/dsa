from heap import MaxHeap, MinHeap

def findMedian(array):

    # initialise left (max heap) and right (min heap)
    left = MaxHeap()
    right = MinHeap()

    # store array[0] in left.root 
    left.insert(array[0])

    # loop array from 1
    for i in range(1, len(array)):

        # if value > left.root (i.e to right of left.root), store in right.root
        if array[i] > left.nodes[0]:
            right.insert(array[i])
        # else, insert into left
        else:
            left.insert(array[i])

        # balance left and right
        if (left.count + right.count) % 2 == 0:
            if left.count > right.count:
                value = left.remove()
                right.insert(value)
        else:
            if right.count > left.count:
                value = right.remove()
                left.insert(value)
        
    # if odd, return left.root
    if (left.count + right.count) % 2 == 0:
        return (left.nodes[0] + right.nodes[0]) / 2
    # else return (left.root + right.root) / 2 
    else:
        return left.nodes[0]

print(findMedian([1, 2])) # 1.5
print(findMedian([1, 2, 3])) # 2