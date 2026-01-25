def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0][:]
    
    for i in range(1, N):
        for j in range(4):
            if j < 3: dp[i][j] = max(*dp[i - 1][:j], *dp[i - 1][j + 1:]) + land[i][j]
            else: dp[i][j] = max(dp[i - 1][:j]) + land[i][j]
    
    return max(dp[-1])