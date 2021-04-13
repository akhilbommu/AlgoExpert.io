def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i, j = 0, 0
    m, n = len(arrayOne), len(arrayTwo)
    min_result = float('inf')
    pair = [-1, -1]

    while i < m and j < n:
        if abs(arrayOne[i] - arrayTwo[j]) < min_result:
            min_result = abs(arrayOne[i] - arrayTwo[j])
            pair = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    return pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
print(smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]))
