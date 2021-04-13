def numberOfWaysToMakeChange(n, denoms):
    ways_array = [0] * (n + 1)
    ways_array[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways_array[amount] += ways_array[amount - denom]
        print(ways_array)
    return ways_array[-1]


print(numberOfWaysToMakeChange(6, [1, 5]))
print(numberOfWaysToMakeChange(10, [1, 5, 10, 25]))