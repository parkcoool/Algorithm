import sys
from collections import deque

KNIGHT = ((-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, -2), (1, 2))
NORMAL = ((0, 1), (0, -1), (-1, 0), (1, 0))

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(H)]

# visited[y][x][k]: 말의 움직임으로 k번 움직였을 때 (y, x)를 도달한 적 있는지 여부
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = True

# (y, x, k, movements)
q = deque([(0, 0, 0, 0)])
ans = -1
while q:
  y, x, k, movements = q.popleft()
  
  if y == H - 1 and x == W - 1:
    ans = movements
    break

  if k < K:
    for dy, dx in KNIGHT:
      ny, nx = y + dy, x + dx
      if not (0 <= ny < H and 0 <= nx < W): continue
      if visited[ny][nx][k + 1]: continue
      if grid[ny][nx] == 1: continue
      visited[ny][nx][k + 1] = True
      q.append((ny, nx, k + 1, movements + 1))

  for dy, dx in NORMAL:
    ny, nx = y + dy, x + dx
    if not (0 <= ny < H and 0 <= nx < W): continue
    if visited[ny][nx][k]: continue
    if grid[ny][nx] == 1: continue
    visited[ny][nx][k] = True
    q.append((ny, nx, k, movements + 1))

print(ans)