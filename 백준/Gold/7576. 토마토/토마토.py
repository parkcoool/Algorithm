from collections import deque

M, N = map(int, input().split())

# 1: 익은 토마토  0: 익지 않은 토마토  -1: 빈 칸
grid = [[-1] * M for _ in range(N)]
queue = deque([])
# 익은 토마토 개수
ig = 0
# 총 토마토 개수
tomato = 0

for y in range(N):
  nums = list(map(int, input().split()))
  for x in range(M):
    if nums[x] == 1:
      queue.append((y, x, 0))
      ig += 1
      tomato += 1
    elif nums[x] == 0:
      tomato += 1
    grid[y][x] = nums[x]

ans = 0
while len(queue) > 0:
  y, x, day = queue.popleft()
  ans = day
  
  for y_add, x_add in ((1, 0), (0, 1), (-1, 0), (0, -1)):
    if not (0 <= y + y_add < N and 0 <= x + x_add < M):
      continue
    if grid[y + y_add][x + x_add] != 0:
      continue
    grid[y + y_add][x + x_add] = 1
    ig += 1
    queue.append((y + y_add, x + x_add, day + 1))

print(-1 if ig != tomato else ans)
