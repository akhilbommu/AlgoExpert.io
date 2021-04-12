def minimumWaitingTime(queries):
    queries.sort()
    result = 0
    for i in range(1, len(queries)):
        result += sum(queries[:i])
    return result


print(minimumWaitingTime([3, 2, 1, 2, 6]))
print(minimumWaitingTime([1, 1, 1, 1, 1]))
