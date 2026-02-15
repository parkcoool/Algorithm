import sys

input = sys.stdin.readline

C, N = map(int, input().strip().split())
cities = [list(map(int, input().strip().split())) for _ in range(N)]

# dp[i]: 고객을 i명 늘리기 위한 최소 비용
dp = [float("inf")] * (C + 1)
dp[0] = 0

for i in range(0, C):
  for cost, reward in cities:
    j = min(C, i + reward)
    dp[j] = min(dp[j], dp[i] + cost)

print(dp[C])