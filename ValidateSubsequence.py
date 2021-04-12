def isValidSubsequence(array, sequence):
    array_pointer,sequence_pointer = 0,0
    while array_pointer < len(array) and sequence_pointer < len(sequence):
        if array[array_pointer] == sequence[sequence_pointer]:
            sequence_pointer += 1
        array_pointer += 1
    return sequence_pointer == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [25]))
