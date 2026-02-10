import sys

input = sys.stdin.readline

board = list([list(map(int, input().strip())) for _ in range(9)])

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
blocks = [set() for _ in range(9)]

zeros = []

for y in range(9):
  for x in range(9):
    num = board[y][x]
    if num == 0:
      zeros.append((y, x))

    rows[y].add(num)
    cols[x].add(num)
    block_index = (y // 3) * 3 + (x // 3)
    blocks[block_index].add(num)

def dfs(zero_index):
  if zero_index >= len(zeros): return True
  
  y, x = zeros[zero_index]
  block_index = (y // 3) * 3 + (x // 3)

  for n in range(1, 10):
    if n in rows[y]: continue
    if n in cols[x]: continue
    if n in blocks[block_index]: continue

    board[y][x] = n
    rows[y].add(n)
    cols[x].add(n)
    blocks[block_index].add(n)
    result = dfs(zero_index + 1)
    if result: return True
    board[y][x] = 0
    rows[y].discard(n)
    cols[x].discard(n)
    blocks[block_index].discard(n)

  return False

dfs(0)

for row in board:
  print(*row, sep="")