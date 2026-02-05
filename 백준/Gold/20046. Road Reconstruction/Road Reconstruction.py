import sys
import heapq

INF = float("inf")
input = sys.stdin.readline

M, N = map(int, input().split())
# 0: 도로, 1: 비용 1 공터, 2: 비용 2 공터, -1: 건설 불가
grid = [list(map(int, input().split())) for _ in range(M)]

def solution():
  if grid[0][0] == -1:
    return -1

  dp = [[INF] * N for _ in range(M)]
  dp[0][0] = grid[0][0]

  # (cost, y, x)
  pq = [(grid[0][0], 0, 0)]
  while pq:
    cost, y, x = heapq.heappop(pq)
    cost = dp[y][x]

    if dp[y][x] < cost:
      continue

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      ny, nx = y + dy, x + dx
      if not (0 <= ny < M): continue
      if not (0 <= nx < N): continue
      if grid[ny][nx] == -1: continue
        
      new_cost = cost + grid[ny][nx]
      if new_cost >= dp[ny][nx]: continue

      dp[ny][nx] = new_cost
      heapq.heappush(pq, (new_cost, ny, nx))

  ans = dp[M - 1][N - 1]
  if ans == INF: return -1
  else: return ans

print(solution())