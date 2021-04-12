def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))
print(insertionSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))
