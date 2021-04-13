def numberOfWaysToTraverseGraph(width, height):
    dp = [[0 for i in range(width)] for j in range(height)]
    for i in range(width):
        dp[0][i] = 1
    for j in range(height):
        dp[j][0] = 1
    print(dp)
    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print(numberOfWaysToTraverseGraph(4, 3))
print(numberOfWaysToTraverseGraph(2, 3))
