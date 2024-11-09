import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
start = (0, 0)

for y in range(n):
  nums = list(map(int, input().split()))
  for x in range(m):
    if nums[x] == 2:
      start = (y, x)
    elif nums[x] == 0:
      dp[y][x] = 0
    grid[y][x] = nums[x]

queue = deque([(start[0], start[1], 0)])
dist = 0

while len(queue) > 0:
  y, x, dist = queue.popleft()

  if grid[y][x] == 0:
    continue

  if dp[y][x] != -1:
    continue

  dp[y][x] = dist
  dist += 1

  if y > 0: queue.append((y - 1, x, dist))
  if x > 0: queue.append((y, x - 1, dist))
  if y < n - 1: queue.append((y + 1, x, dist))
  if x < m - 1: queue.append((y, x + 1, dist))

for row in dp:
  print(" ".join(map(str, row)))