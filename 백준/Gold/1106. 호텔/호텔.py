import sys

input = sys.stdin.readline

C, N = map(int, input().strip().split())
cities = [list(map(int, input().strip().split())) for _ in range(N)]

# dp[i]: i명의 고객을 늘리기 위해 투자해야 하는 돈의 최솟값
dp = [float("inf")] * (C + 1)
dp[0] = 0

ans = float("inf")
for current_value in range(C + 1):
  for j in range(N):
      cost, value = cities[j]
      next_value = current_value + value
      
      if next_value > C:
        ans = min(ans, dp[current_value] + cost)
      else:
        dp[next_value] = min(dp[next_value], dp[current_value] + cost)

ans = min(ans, dp[C])
print(ans)