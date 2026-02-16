import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, L, R = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]

def find(parents, y, x):
  parent = parents[y][x]
  py, px = parent
  
  if parent == (y, x): return (y, x)
  result = find(parents, py, px)
  parents[y][x] = result
  
  return result
  
def union(parents, y1, x1, y2, x2):
  parent1 = find(parents, y1, x1)
  py1, px1 = parent1
  parent2 = find(parents, y2, x2)
  py2, px2 = parent2
  
  if parent1 > parent2:
    parents[py2][px2] = parent1
  else:
    parents[py1][px1] = parent2

ans = 0
while True:
  parents = [[(y, x) for x in range(N)] for y in range(N)]
  # [population, count]
  populations = defaultdict(lambda: [0, 0])

  again = False

  # 국경선 열기
  for y in range(N):
    for x in range(N):
      for ny, nx in ((y + 1, x), (y, x + 1)):
        if ny >= N or nx >= N: continue
        if L <= abs(grid[ny][nx] - grid[y][x]) <= R:
          union(parents, y, x, ny, nx)

  # 인구 합치기
  for y in range(N):
    for x in range(N):
      parent = find(parents, y, x)
      populations[parent][0] += grid[y][x]
      populations[parent][1] += 1

  # 인구 분배하기
  for y in range(N):
    for x in range(N):
      parent = find(parents, y, x)
      population, count = populations[parent]

      divided = population // count
      if grid[y][x] != divided:
        grid[y][x] = divided
        again = True
  
  if not again: break
  ans += 1
print(ans)