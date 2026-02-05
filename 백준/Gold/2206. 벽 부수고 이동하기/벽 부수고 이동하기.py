from collections import deque

OFFSETS = ((1, 0), (0, 1), (-1, 0), (0, -1))

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# dp_1[y][x] = (y, x)에서 목적지까지 가는 최단 거리
dp_1 = [[-1] * M for _ in range(N)]
dp_1[N - 1][M - 1] = 0

# dp_2[y][x] = 시작점에서 (y, x)까지 가는 최단 거리
dp_2 = [[-1] * M for _ in range(N)]
dp_2[0][0] = 1


def explore(y, x, dp):
  q = deque([(y, x)])
  while q:
    y, x = q.popleft()

    for y_offset, x_offset in OFFSETS:
      new_y, new_x = y + y_offset, x + x_offset
      if not (0 <= new_y < N and 0 <= new_x < M):
        continue
      if dp[new_y][new_x] != -1:
        continue
      if grid[new_y][new_x] != 0:
        continue
      q.append((new_y, new_x))
      dp[new_y][new_x] = dp[y][x] + 1


explore(N - 1, M - 1, dp_1)
explore(0, 0, dp_2)

if N + M == 3:
  print(2)
  exit()

if N + M == 2:
  print(1)
  exit()

ans = -1
for y in range(N):
  for x in range(M):
    for y_offset_1, x_offset_1 in OFFSETS:
      y1, x1 = y + y_offset_1, x + x_offset_1
      if not (0 <= y1 < N and 0 <= x1 < M):
        continue
        
      for y_offset_2, x_offset_2 in OFFSETS:
        y2, x2 = y + y_offset_2, x + x_offset_2
        if y1 == y2 and x1 == x2:
          continue
        
        if not (0 <= y2 < N and 0 <= x2 < M):
          continue
  
        if dp_1[y1][x1] != -1 and dp_2[y2][x2] != -1:
          result = dp_1[y1][x1] + dp_2[y2][x2] + 2
          if result < ans or ans == -1:
            ans = result

print(ans)
