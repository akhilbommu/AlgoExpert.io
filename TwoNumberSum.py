def twoNumberSum(array, targetSum):
    # Write your code here.
    res_array = []
    for i in range(len(array)):
        if targetSum-array[i] in array[:i] or targetSum-array[i] in array[i+1:]:
            res_array.append(array[i])
            res_array.append(targetSum-array[i])
            break
    return res_array


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5))

