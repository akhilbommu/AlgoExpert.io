def isMonotonic(array):
    isNonIncreasing = False
    isNonDecreasing = False
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isNonDecreasing = True
        elif array[i] < array[i - 1]:
            isNonIncreasing = True
        else:
            continue
        if isNonDecreasing and isNonIncreasing:
            return False
    return True


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
print(isMonotonic([-1, -5, -10, -1100, -900, -1101, -1102, -9001]))