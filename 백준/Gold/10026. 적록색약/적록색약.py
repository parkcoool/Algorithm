from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N = int(input())
grid1 = [list(input()) for _ in range(N)]
grid2 = [grid1[i][:] for i in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
ans1, ans2 = 0, 0

def dfs1(y, x, color):
  grid1[y][x] = ""
  for i in range(4):
    new_y, new_x = y + dy[i], x + dx[i]
    if not(0 <= new_y < N and 0 <= new_x < N): continue
    if grid1[new_y][new_x] != color: continue
    dfs1(new_y, new_x, color)

for y in range(N):
  for x in range(N):
    if grid1[y][x] != "":
      dfs1(y, x, grid1[y][x])
      ans1 += 1

def dfs2(y, x, color):
  grid2[y][x] = ""
  for i in range(4):
    new_y, new_x = y + dy[i], x + dx[i]
    if not(0 <= new_y < N and 0 <= new_x < N): continue
    new_color = grid2[new_y][new_x]
    if not((color == "R" or color == "G") and (new_color == "R" or new_color == "G")) and new_color != color: continue
    dfs2(new_y, new_x, color)

for y in range(N):
  for x in range(N):
    if grid2[y][x] != "":
      dfs2(y, x, grid2[y][x])
      ans2 += 1

print(ans1, ans2)