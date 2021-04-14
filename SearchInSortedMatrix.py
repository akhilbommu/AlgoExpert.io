def searchInSortedMatrix(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
print(searchInSortedMatrix(matrix,44))
print(searchInSortedMatrix(matrix,1004))
print(searchInSortedMatrix(matrix,-1))
