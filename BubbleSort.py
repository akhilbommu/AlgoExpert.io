def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
    return array


print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))
print(bubbleSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))
