import sys
from collections import deque

INF = float("inf")
input = sys.stdin.readline

N, M = map(int, input().split())

teachers = []
s = ()
j = ()
grid = []

for y in range(N):
  row = list(input())
  for x in range(M):
    if row[x] == "T":
      teachers.append((y, x))
    elif row[x] == "S":
      s = (y, x)
    elif row[x] == "J":
      j = (y, x)
  grid.append(row)

def get_dist_table(start):
  q = deque([start])
  dist_table = [[INF] * M for _ in range(N)]
  dist_table[start[0]][start[1]] = 0
  
  while q:
    y, x = q.popleft()
    dist = dist_table[y][x]
      
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      ny, nx = y + dy, x + dx
      if not (0 <= ny < N): continue
      if not (0 <= nx < M): continue
      if grid[ny][nx] == "#": continue
      if dist_table[ny][nx] != INF: continue
      dist_table[ny][nx] = dist + 1
      q.append((ny, nx))

  return dist_table

dist_table_s = get_dist_table(s)
dist_table_j = get_dist_table(j)

ans = INF
for t in teachers:
  dist1 = dist_table_s[t[0]][t[1]]
  dist2 = dist_table_j[t[0]][t[1]] * 2
  ans = min(ans, dist1 + dist2)
ans = min(ans, dist_table_s[j[0]][j[1]] * 2)

if ans == INF: print(-1)
else: print(ans)