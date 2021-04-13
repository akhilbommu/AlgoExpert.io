def productSum(array,depth=1):
    totalSum = 0
    for each in array:
        if type(each) is list:
            totalSum += productSum(each,depth+1)
        else:
            totalSum += each
    return totalSum * depth


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
print(productSum([9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]))