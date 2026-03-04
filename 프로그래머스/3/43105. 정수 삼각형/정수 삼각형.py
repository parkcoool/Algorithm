def solution(triangle):
    # dp[i][j]: 꼭대기에서 (i, j)까지의 최댓값
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j > 0: dp[i][j] = dp[i - 1][j - 1]
            if j < i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
            dp[i][j] += triangle[i][j]
    
    return max(dp[-1])