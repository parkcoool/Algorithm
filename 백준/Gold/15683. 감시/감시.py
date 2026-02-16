import sys
from itertools import product

DIRECTIONS = ["U", "R", "D", "L"]
input = sys.stdin.readline

N, M = map(int, input().strip().split())

# (번호, y, x)
cameras = []
grid = []
for y in range(N):
  row = list(map(int, input().strip().split()))
  grid.append(row)
  
  for x, num in enumerate(row):
    if 1 <= num <= 5:
      cameras.append((num, y, x))
      grid[y][x] = 0
    elif num == 6:
      grid[y][x] = -1

ans = N * M

def fill(grid, y, x, direction):
  dy = 1 if direction == "D" else -1 if direction == "U" else 0
  dx = 1 if direction == "R" else -1 if direction == "L" else 0

  while 0 <= y < N and 0 <= x < M and grid[y][x] != -1:
    grid[y][x] = 1
    y += dy
    x += dx

for rotates in product(range(4), repeat=len(cameras)):
  temp_grid = [row[:] for row in grid]

  for (num, y, x), rotate in zip(cameras, rotates):
    temp_grid[y][x] = 1
    
    # 1번 카메라
    if num == 1:
      fill(temp_grid, y, x, DIRECTIONS[rotate])

    # 2번 카메라
    elif num == 2:
      rotate %= 2
      fill(temp_grid, y, x, DIRECTIONS[rotate])
      fill(temp_grid, y, x, DIRECTIONS[rotate + 2])

    # 3번 카메라
    elif num == 3:
      fill(temp_grid, y, x, DIRECTIONS[rotate])
      fill(temp_grid, y, x, DIRECTIONS[(rotate + 1) % 4])

    # 4번 카메라
    elif num == 4:
      fill(temp_grid, y, x, DIRECTIONS[rotate])
      fill(temp_grid, y, x, DIRECTIONS[(rotate + 1) % 4])
      fill(temp_grid, y, x, DIRECTIONS[(rotate + 2) % 4])

    # 5번 카메라
    elif num == 5:
      for direction in DIRECTIONS:
        fill(temp_grid, y, x, direction)

  count = sum([row.count(0) for row in temp_grid])
  ans = min(ans, count)

print(ans)