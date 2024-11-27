import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = items[i]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else: 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])