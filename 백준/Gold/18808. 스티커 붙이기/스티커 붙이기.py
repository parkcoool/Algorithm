import sys

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
board = [[0] * M for _ in range(N)]

# 스티커를 board의 (y, x)에 붙이는 함수
def attach(board, y, x, sticker):
  temp_board = [row[:] for row in board]
  
  for dy in range(r):
    for dx in range(c):
      ny, nx = y + dy, x + dx
      if sticker[dy][dx] == 1:
        if board[ny][nx] == 1: return False
        temp_board[ny][nx] = 1
      
  return temp_board

for _ in range(K):
  r, c = map(int, input().strip().split())
  sticker = [list(map(int, input().strip().split())) for _ in range(r)]

  success = False

  for _ in range(4):
    for y in range(N - r + 1):
      for x in range(M - c + 1):
        result = attach(board, y, x, sticker)
        if result:
          board = result
          success = True
          break
      if success: break  
    if success: break
    new_sticker = [[0] * r for _ in range(c)]
    for y in range(r):
      for x in range(c):
        new_sticker[x][r - y - 1] = sticker[y][x]
    sticker = new_sticker
    r, c = c, r

print(sum([sum(row) for row in board]))