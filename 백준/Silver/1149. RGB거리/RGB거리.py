N = int(input())

COSTS = []
dp = [[0] * 3 for _ in range(N)]
for _ in range(N):
    COSTS.append(tuple(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = COSTS[0][0], COSTS[0][1], COSTS[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] + COSTS[i][0], dp[i - 1][2] + COSTS[i][0])
    dp[i][1] = min(dp[i - 1][0] + COSTS[i][1], dp[i - 1][2] + COSTS[i][1])
    dp[i][2] = min(dp[i - 1][0] + COSTS[i][2], dp[i - 1][1] + COSTS[i][2])

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
