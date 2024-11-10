import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# cumsum[y][x]: grid[0][x] ~ grid[y][x]까지 합
cumsum = [[0] * N for _ in range(N)]
for x in range(N):
  cumsum[0][x] = grid[0][x]
  for y in range(1, N):
    cumsum[y][x] = cumsum[y - 1][x] + grid[y][x]

# dp[y][x]: (0, 0)부터 (y, x)까지 합
dp = [[0] * N for _ in range(N)]
for y in range(N):
  for x in range(N):
    dp[y][x] = cumsum[y][x]
    if x > 0: dp[y][x] += dp[y][x - 1]

for _ in range(M):
  y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
  result = dp[y2][x2]
  if y1 > 0: result -= dp[y1 - 1][x2]
  if x1 > 0: result -= dp[y2][x1 - 1]
  if y1 > 0 and x1 > 0:
    result += dp[y1 - 1][x1 - 1]
  print(result)