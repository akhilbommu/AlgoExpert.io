import sys


def findThreeLargestNumbers(array):
    first_max, second_max, third_max = -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1
    for i in range(len(array)):
        if array[i] > first_max:
            third_max = second_max
            second_max = first_max
            first_max = array[i]
        elif array[i] > second_max:
            third_max = second_max
            second_max = array[i]
        elif array[i] > third_max:
            third_max = array[i]
    return [third_max, second_max, first_max]


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))
