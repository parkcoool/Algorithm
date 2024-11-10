import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  grid = [list(map(int, input().split())) for _ in range(2)]

  #dp[y][x] = (y, x)가 가장 오른쪽 스티커일 때 답
  dp = [[-1] * n for _ in range(2)]
  dp[0][0] = grid[0][0]
  dp[1][0] = grid[1][0]

  if n > 1:
    dp[0][1] = grid[1][0] + grid[0][1]
    dp[1][1] = grid[0][0] + grid[1][1]
  
  for x in range(2, n):
    dp[0][x] = max(dp[1][x - 2], dp[1][x - 1]) + grid[0][x]
    dp[1][x] = max(dp[0][x - 2], dp[0][x - 1]) + grid[1][x]
    
  print(max(dp[0][n - 1], dp[1][n - 1]))
