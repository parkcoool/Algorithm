import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(N)]

parents = [[(y, x) for x in range(M)] for y in range(N)]

def find(y, x):
  parent = parents[y][x]
  if parent == (y, x): return (y, x)
  parents[y][x] = find(parent[0], parent[1])
  return parents[y][x]

def union(y1, x1, y2, x2):
  root1 = find(y1, x1)
  root2 = find(y2, x2)

  if root1 <= root2:
    parents[root2[0]][root2[1]] = root1
  else:
    parents[root1[0]][root1[1]] = root2

for y in range(N):
  for x in range(M):
    direction = grid[y][x]

    if direction == "U":
      union(y, x, y - 1, x)
    elif direction == "R":
      union(y, x, y, x + 1)
    elif direction == "D":
      union(y, x, y + 1, x)
    else:
      union(y, x, y, x - 1)

ans = 0
for y in range(N):
  for x in range(M):
    if find(y, x) == (y, x):
      ans += 1

print(ans)