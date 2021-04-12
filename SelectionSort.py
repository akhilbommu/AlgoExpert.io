def selectionSort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]
    return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
print(selectionSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))