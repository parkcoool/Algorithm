import sys

input = sys.stdin.readline

C, N = map(int, input().strip().split())
cities = [list(map(int, input().strip().split())) for _ in range(N)]

# dp[i]: i명의 고객을 늘리기 위해 투자해야 하는 돈의 최솟값
dp = [float("inf")] * (C + 1)
dp[0] = 0

for current_value in range(C + 1):
  for j in range(N):
    multiplier = 1
    while True:
      cost, value = cities[j]
      cost *= multiplier
      value *= multiplier

      next_value = current_value + value
      
      if next_value >= C:
        dp[C] = min(dp[C], dp[current_value] + cost)
        break
      dp[next_value] = min(dp[next_value], dp[current_value] + cost)
      multiplier += 1

print(dp[C])