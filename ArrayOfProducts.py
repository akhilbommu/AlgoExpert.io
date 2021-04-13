def arrayOfProducts(array):
    result_array = [1] * len(array)
    for i in range(1,len(array)):
        result_array[i] = result_array[i-1] * array[i-1]
    temp = 1
    for i in range(len(array)-1,-1,-1):
        result_array[i] = result_array[i] * temp
        temp *= array[i]
    return result_array


print(arrayOfProducts([1, 8, 6, 2, 4]))
print(arrayOfProducts([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
