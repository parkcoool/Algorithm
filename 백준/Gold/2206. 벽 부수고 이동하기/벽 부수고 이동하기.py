import sys
from collections import deque

INF = float("inf")
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# dp[y][x][0]: 벽을 부수지 않았을 때 (y, x)까지의 최단 거리
# dp[y][x][1]: 벽을 부쉈을 때 (y, x)까지의 최단 거리
dp = [[[INF, INF] for _ in range(M)] for _ in range(N)]
dp[0][0][0] = 1
dp[0][0][1] = 1

q = deque([(0, 0)])
while q:
  y, x = q.popleft()
  cost1, cost2 = dp[y][x]

  for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    ny, nx = y + dy, x + dx
    if not (0 <= ny < N): continue
    if not (0 <= nx < M): continue

    skip = True
    
    if grid[ny][nx] == 0:
      if cost1 + 1 < dp[ny][nx][0]:
        dp[ny][nx][0] = cost1 + 1
        skip = False
      if cost2 + 1 < dp[ny][nx][1]:
        dp[ny][nx][1] = cost2 + 1
        skip = False

    else:
      if cost1 + 1 < dp[ny][nx][1]:
        dp[ny][nx][1] = cost1 + 1
        skip = False

    if not skip:
      q.append((ny, nx))

ans = min(dp[N - 1][M - 1])
if ans == INF: print(-1)
else: print(ans)