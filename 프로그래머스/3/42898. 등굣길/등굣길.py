def solution(m, n, puddles):
    # dp[y][x]: (1, 1)에서 (y, x)까지 오는 경우의 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles: continue
            if y == 1 and x == 1: continue
            dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
    
    return dp[n][m] % 1_000_000_007