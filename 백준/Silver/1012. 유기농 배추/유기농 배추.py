import sys
sys.setrecursionlimit(100000)

def dfs(grid, x, y, M, N):
  grid[y][x] = 0
  if x > 0 and grid[y][x - 1] == 1: dfs(grid, x - 1, y, M, N)
  if y > 0 and grid[y - 1][x] == 1: dfs(grid, x, y - 1, M, N)
  if x < M - 1 and grid[y][x + 1] == 1: dfs(grid, x + 1, y, M, N)
  if y < N - 1 and grid[y + 1][x] == 1: dfs(grid, x, y + 1, M, N)

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  grid = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    grid[y][x] = 1
  ans = 0
  for y in range(N):
    for x in range(M):
      if grid[y][x] == 1:
        dfs(grid, x, y, M, N)
        ans += 1
  print(ans)