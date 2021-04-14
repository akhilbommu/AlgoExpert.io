def threeNumberSort(array, order):
    firstIndex,lastIndex = 0,len(array)-1
    for i in range(len(array)):
        if array[i] == order[0]:
            array[firstIndex],array[i] = array[i],array[firstIndex]
            firstIndex += 1
        #print(array,i)

    for i in range(len(array)-1,-1,-1):
        if array[i] == order[-1]:
            array[lastIndex],array[i] = array[i],array[lastIndex]
            lastIndex -= 1
        #print(array,i)
    return array


def threeNumberSort2(array, order):
    firstIndex, secondIndex, thirdIndex = 0, 0, len(array) - 1
    while secondIndex <= thirdIndex:
        curr_val = array[secondIndex]
        if curr_val == order[0]:
            array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]
            firstIndex += 1
            secondIndex += 1
        elif curr_val == order[-1]:
            array[thirdIndex], array[secondIndex] = array[secondIndex], array[thirdIndex]
            thirdIndex -= 1
        else:
            secondIndex += 1
    return array


print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
print(threeNumberSort2([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))

print(threeNumberSort([-2, -3, -3, -3, -3, -3, -2, -2, -3], [-2, -3, 0]))
print(threeNumberSort2([-2, -3, -3, -3, -3, -3, -2, -2, -3], [-2, -3, 0]))

print(threeNumberSort([], [0, 7, 9]))
print(threeNumberSort2([], [0, 7, 9]))