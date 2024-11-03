import sys

sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]

memo = [[-1] * N for _ in range(M)]


def dfs(y, x):
  if y == M - 1 and x == N - 1:
    return 1

  if memo[y][x] != -1:
    return memo[y][x]

  current = MAP[y][x]
  count = 0
  if y > 0 and MAP[y - 1][x] < current:
    count += dfs(y - 1, x)
  if x < N - 1 and MAP[y][x + 1] < current:
    count += dfs(y, x + 1)
  if y < M - 1 and MAP[y + 1][x] < current:
    count += dfs(y + 1, x)
  if x > 0 and MAP[y][x - 1] < current:
    count += dfs(y, x - 1)

  memo[y][x] = count
  return count

print(dfs(0, 0))