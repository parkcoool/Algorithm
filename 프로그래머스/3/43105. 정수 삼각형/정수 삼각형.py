def solution(triangle):
    dp = [row[:] for row in triangle]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = dp[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]
        