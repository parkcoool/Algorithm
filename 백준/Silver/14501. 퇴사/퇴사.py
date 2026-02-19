import sys

input = sys.stdin.readline

N = int(input())
tasks = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [0] * (N + 1)
for day, (time, price) in enumerate(tasks):
  for next_day in range(day + time, N + 1):
    dp[next_day] = max(dp[next_day], dp[day] + price)

print(max(dp))