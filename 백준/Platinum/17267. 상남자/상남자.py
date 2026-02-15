import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
L, R = map(int, input().strip().split())

# (y, x, l, r)
q = deque([])
grid = []

for y in range(N):
  row = list(map(int, input().strip()))
  grid.append(row)
  for x, num in enumerate(row):
    if num == 2:
      q.append((y, x, L, R))

ans = 0
while q:
  y, x, l, r = q.popleft()

  for direction in (-1, 1):
    for dy in range(N):
      if dy == 0 and direction == 1: continue
      
      ny = y + dy * direction
      if not (0 <= ny < N): break
      if grid[ny][x] == 1: break

      grid[ny][x] = 1
      ans += 1
  
      for dx in (-1, 1):
        nx = x + dx
        if not (0 <= nx < M): continue
        if grid[ny][nx] == 1: continue

        if l > 0 and dx == -1:
          q.append((ny, nx, l - 1, r))
        elif r > 0 and dx == 1:
          q.append((ny, nx, l, r - 1))

print(ans)