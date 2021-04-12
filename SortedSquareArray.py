def sortedSquaredArray(array):
    output_array = [0] * len(array)
    start, end = 0, len(array) - 1
    j = len(array) - 1
    while start <= end:
        if array[start] ** 2 > array[end] ** 2:
            output_array[j] = array[start] ** 2
            start += 1
        else:
            output_array[j] = array[end] ** 2
            end -= 1
        j -= 1
    return output_array

print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-10, -5, 0, 5, 10]))