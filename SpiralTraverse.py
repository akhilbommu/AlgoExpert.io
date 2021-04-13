def spiralTraverse(matrix):
    nums = []
    if len(matrix) == 0 or matrix is None:
        return nums
    m, n = len(matrix), len(matrix[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while len(nums) < m * n:
        for i in range(left, right + 1):
            if len(nums) < m * n:
                nums.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            if len(nums) < m * n:
                nums.append(matrix[i][right])
        right -= 1
        for i in range(right, left - 1, -1):
            if len(nums) < m * n:
                nums.append(matrix[bottom][i])
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if len(nums) < m * n:
                nums.append(matrix[i][left])
        left += 1
    return nums


print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
