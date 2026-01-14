import sys
sys.setrecursionlimit(10**6)

N = int(input())
grid = []
for _ in range(N):
  grid.append(list(map(int, list(input()))))

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def dfs(y, x):
  grid[y][x] = 0
  count = 1
  for i in range(4):
    new_y, new_x = y + dy[i], x + dx[i]
    if not(0 <= new_y < N and 0 <= new_x < N): continue
    if grid[new_y][new_x] != 1: continue
    count += dfs(new_y, new_x)
  return count

ans = []
for y in range(N):
  for x in range(N):
    if grid[y][x] != 1: continue
    ans.append(dfs(y, x))

print(len(ans))
print(*sorted(ans), sep="\n")
