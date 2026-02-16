import sys

input = sys.stdin.readline

N, M, y, x, K = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
moves = list(map(int, input().strip().split()))

# dice[2]: 윗면, dice[5]: 바닥면
dice = [0] * 6

for move in moves:
  dy = -1 if move == 3 else 1 if move == 4 else 0
  dx = -1 if move == 2 else 1 if move == 1 else 0
  ny, nx = y + dy, x + dx
  if not (0 <= ny < N): continue
  if not (0 <= nx < M): continue

  if move == 1:
    dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
  elif move == 2:
    dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
  elif move == 3:
    dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
  elif move == 4:
    dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]

  if grid[ny][nx] == 0:
    grid[ny][nx] = dice[5]
  else:
    dice[5] = grid[ny][nx]
    grid[ny][nx] = 0

  y, x = ny, nx

  print(dice[2])