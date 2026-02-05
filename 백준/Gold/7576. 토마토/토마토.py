import sys

input = sys.stdin.readline

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

stack = []
for y in range(N):
  for x in range(M):
    if grid[y][x] == 1: stack.append((y, x))

ans = 0
count = sum([row.count(0) for row in grid])
while True:
  if count == 0:
    print(ans)
    break
    
  if not stack:
    print(-1)
    break

  next_stack = []
  while stack:
    y, x = stack.pop()
    for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
      ny, nx = y + dy, x + dx
      if not (0 <= ny < N): continue
      if not (0 <= nx < M): continue
      if grid[ny][nx] != 0: continue
      grid[ny][nx] = 1
      next_stack.append((ny, nx))
      count -= 1
    
  stack = next_stack
  ans += 1