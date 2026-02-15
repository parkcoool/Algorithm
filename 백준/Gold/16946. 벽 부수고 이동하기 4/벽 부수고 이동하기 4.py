import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# space_ids[y][x]: (y, x)가 속한 공간의 id
space_ids = [[0] * M for _ in range(N)]
last_space_id = 0

# spaces[id]: 공간 id의 공간 넓이
spaces = [0]

for y in range(N):
  for x in range(M):
    if grid[y][x] == 1: continue
    if space_ids[y][x] != 0: continue

    last_space_id += 1
    path = []

    def dfs(y, x):
      space = 1
      space_ids[y][x] = last_space_id
      path.append((y, x))
      
      for dy, dx in ((-1, 0), (0, 1), (0, -1), (1, 0)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N): continue
        if not (0 <= nx < M): continue
        if grid[ny][nx] == 1: continue
        if space_ids[ny][nx] != 0: continue
        space += dfs(ny, nx)
      
      return space

    spaces.append(dfs(y, x))
    for ny, nx in path:
      space_ids[ny][nx] = last_space_id

for y in range(N):
  for x in range(M):
    if grid[y][x] == 0: continue

    near_space_ids = set()
    if y > 0: near_space_ids.add(space_ids[y - 1][x])
    if x > 0: near_space_ids.add(space_ids[y][x - 1])
    if y + 1 < N: near_space_ids.add(space_ids[y + 1][x])
    if x + 1 < M: near_space_ids.add(space_ids[y][x + 1])

    ans = 1
    for space_id in near_space_ids:
      space = spaces[space_id]
      ans += space
      
    grid[y][x] = ans % 10

for row in grid:
  print(*row, sep="")