import sys

input = sys.stdin.readline

N = int(input())
recs = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]
dp[0][0] = recs[0][0]
dp[0][1] = recs[0][1]

for i, (a, b) in enumerate(recs):
  if i == 0: continue

  # 가로: a, 세로: b
  dp[i][0] = max(
    dp[i - 1][0] + a + abs(b - recs[i - 1][1]),
    dp[i - 1][1] + a + abs(b - recs[i - 1][0])
  )

  # 가로: b, 세로: a
  dp[i][1] = max(
    dp[i - 1][0] + b + abs(a - recs[i - 1][1]),
    dp[i - 1][1] + b + abs(a - recs[i - 1][0])
  )

print(max(dp[-1]))