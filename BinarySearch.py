def binarySearch(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))