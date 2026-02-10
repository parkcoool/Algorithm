import sys
from itertools import product

input = sys.stdin.readline

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def combine(table, direction):
  size = len(table)

  for i in range(size):    
    for j in range(size):
      x, y = 0, 0
      nx, ny = 0, 0
      
      if direction == UP:
        x, y = i, j
        nx, ny = x, y - 1
          
      elif direction == DOWN:
        x, y = i, size - 1 - j
        nx, ny = x, y + 1
          
      elif direction == LEFT:
        x, y = j, i
        nx, ny = x - 1, y
          
      elif direction == RIGHT:
        x, y = size - 1 - j, i
        nx, ny = x + 1, y

      if not (0 <= ny < size): continue
      if not (0 <= nx < size): continue
      if table[y][x] != table[ny][nx]: continue
      table[y][x] = 0
      table[ny][nx] *= 2

def move(table, direction):
  size = len(table)

  for i in range(size):
    k = 0
    
    for j in range(size):
      x, y = 0, 0
      last = 0
      
      if direction == UP:
        x, y = i, j
        last = k
          
      elif direction == DOWN:
        x, y = i, size - 1 - j
        last = size - 1 - k
          
      elif direction == LEFT:
        x, y = j, i
        last = k
          
      elif direction == RIGHT:
        x, y = size - 1 - j, i
        last = size - 1 - k
          
      if table[y][x] != 0:
        k += 1
        if direction in (UP, DOWN):
          table[last][x], table[y][x] = table[y][x], table[last][x]
        else:
          table[y][last], table[y][x] = table[y][x], table[y][last]
        
          
N = int(input())
table = list([list(map(int, input().strip().split())) for _ in range(N)])

ans = 0
for directions in product((UP, RIGHT, DOWN, LEFT), repeat=5):
  temp_table = [row[:] for row in table]

  for direction in directions:
    move(temp_table, direction)
    combine(temp_table, direction)
    move(temp_table, direction)

    ans = max(ans, *[max(row) for row in temp_table])

print(ans)