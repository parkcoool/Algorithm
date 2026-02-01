import sys

input = sys.stdin.readline
M, N = map(int, input().split())
grid = [[1] * M for _ in range(M)]

growth_diffs = [0] * (2 * M - 1)
for _ in range(N):
  zero, one, two = map(int, input().split())
  if one:
    growth_diffs[zero] += 1
  if one and two:
    growth_diffs[zero + one] += 1
  elif not one and two:
    growth_diffs[zero + one] += 2

growths = [0] * (2 * M - 1)
for i, amount in enumerate(growth_diffs):
  if i == 0: growths[i] = growth_diffs[i]
  else: growths[i] = growths[i - 1] + growth_diffs[i]

for i, growth in enumerate(growths):
  grid[max(0, M - 1 - i)][max(0, -M + 1 + i)] += growth
  
for y in range(1, M):
  for x in range(1, M):
    grid[y][x] = grid[0][x]
    
for row in grid:
  print(*row)