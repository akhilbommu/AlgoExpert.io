def kadanesAlgorithm(array):
    maxSum, currentSum = 0, 0
    for i in range(len(array)):
        currentSum += array[i]
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum if maxSum > 0 else -1


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanesAlgorithm([1, 2, -4, 3, 5, -9, 8, 1, 2]))
print(kadanesAlgorithm([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]))