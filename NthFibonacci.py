def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    array = [0] * n
    array[0],array[1] = 0,1
    for i in range(2,n):
        array[i] = array[i-1]+array[i-2]
    return array[-1]

print(getNthFib(2))
print(getNthFib(6))
