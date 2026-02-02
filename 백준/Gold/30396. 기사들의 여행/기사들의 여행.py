import sys
from collections import deque

input = sys.stdin.readline

initial = tuple([tuple(map(int, input().strip())) for _ in range(4)])
target = tuple([tuple(map(int, input().strip())) for _ in range(4)])

visited = set([initial])
q = deque([(initial, 0)])
while q:
  board, count = q.popleft()

  if board == target:
    print(count)
    break

  for y in range(4):
    for x in range(4):
      if board[y][x] != 1: continue
      for dy, dx in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < 4): continue
        if not (0 <= nx < 4): continue
        if board[ny][nx] == 1: continue

        new_board = [list(row) for row in board]
        new_board[y][x] = 0
        new_board[ny][nx] = 1
        new_board = tuple([tuple(row) for row in new_board])

        if new_board in visited: continue
        visited.add(new_board)
        q.append((new_board, count + 1))
      