import sys
from math import ceil

input = sys.stdin.readline

N, M = map(int, input().strip().split())

grid = [[0] * N for _ in range(N)]
for _ in range(M):
  y, x = map(int, input().strip().split())
  grid[y - 1][x - 1] += 1

# zero_count[y + 1][x + 1] = (0, 0) ~ (y, x)까지의 보드에서 0의 개수
zero_count = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(N):
  for x in range(N):
    delta = 1 if grid[y][x] == 0 else 0
    zero_count[y + 1][x + 1] = zero_count[y + 1][x] + delta
    
for y in range(N):
  for x in range(N):
    zero_count[y + 1][x + 1] += zero_count[y][x + 1]

ans = float("inf")

# 블록 개수에 따라 직사각형의 가로 세로 길이 결정
for a in range(1, ceil(M**(1/2)) + 1):
  if M % a != 0: continue
  b = M // a

  for s1, s2 in ((a, b), (b, a)):
    # 보드를 순회하며 필요한 이동 수 계산
    for y in range(N - s1 + 1):
      for x in range(N - s2 + 1):
        # (y, x) ~ (y + s1 - 1, x + s2 - 1)
        count = zero_count[y + s1][x + s2]
        count -= zero_count[y + s1][x]
        count -= zero_count[y][x + s2]
        count += zero_count[y][x]
        
        ans = min(ans, count)

print(ans)