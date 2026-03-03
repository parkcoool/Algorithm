import sys
from collections import deque

KNIGHT = ((-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, -2), (1, 2))
NORMAL = ((0, 1), (0, -1), (-1, 0), (1, 0))

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(H)]

# dp[y][x][k]: 말의 움직임으로 k번 움직였을 때 (y, x)까지의 최소 비용
dp = [[[float("inf")] * (K + 1) for _ in range(W)] for _ in range(H)]
dp[0][0][0] = 0

# (y, x, k, movements)
q = deque([(0, 0, 0, 0)])
while q:
  y, x, k, movements = q.popleft()

  if k < K:
    for dy, dx in KNIGHT:
      ny, nx = y + dy, x + dx
      if not (0 <= ny < H and 0 <= nx < W): continue
      if movements + 1 >= dp[ny][nx][k + 1]: continue
      if grid[ny][nx] == 1: continue
      dp[ny][nx][k + 1] = movements + 1
      q.append((ny, nx, k + 1, movements + 1))

  for dy, dx in NORMAL:
    ny, nx = y + dy, x + dx
    if not (0 <= ny < H and 0 <= nx < W): continue
    if movements + 1 >= dp[ny][nx][k]: continue
    if grid[ny][nx] == 1: continue
    dp[ny][nx][k] = movements + 1
    q.append((ny, nx, k, movements + 1))

ans = min(dp[H - 1][W - 1])
if ans == float("inf"): print(-1)
else: print(ans)