import sys

input = sys.stdin.readline
M, N = map(int, input().split())
grid = [[1] * M for _ in range(M)]

for _ in range(N):
  growths = []
  for num, count in enumerate(map(int, input().split())):
    growths += [num] * count

  for i, growth in enumerate(growths):
    grid[max(0, M - 1 - i)][max(0, -M + 1 + i)] += growth
  
for y in range(1, M):
  for x in range(1, M):
    grid[y][x] = grid[0][x]
    
for row in grid:
  print(*row)