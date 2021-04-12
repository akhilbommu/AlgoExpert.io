def nonConstructibleChange(coins):
    coins = sorted(coins)
    temp = 0
    for each in coins:
        if each > temp + 1:
            break
        temp += each
    return temp+1


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
print(nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100]))
print(nonConstructibleChange([1, 1, 1, 1, 1]))
print(nonConstructibleChange([0, 0, 0, 0, 0]))
