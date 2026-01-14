def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            if y == 0 and x == 0: continue
            if [x + 1, y + 1] in puddles: continue
            count1 = dp[y - 1][x] if y > 0 else 0
            count2 = dp[y][x - 1] if x > 0 else 0
            dp[y][x] = count1 + count2
    return dp[n - 1][m - 1] % 1_000_000_007
    