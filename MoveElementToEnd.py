def moveElementToEnd(array, toMove):
    end = len(array) - 1
    for i in range(len(array)):
        if array[i] == toMove:
            while array[end] == toMove and end > i:
                end -= 1
            array[i], array[end] = array[end], array[i]
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
print(moveElementToEnd([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5))
